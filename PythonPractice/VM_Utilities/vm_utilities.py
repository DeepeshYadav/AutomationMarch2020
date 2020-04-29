import ipaddress
import pytz
from datetime import datetime, date
import threading
from multiprocessing.dummy import Pool
from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVim.task import WaitForTask
import atexit
from pyVmomi import vim, vmodl
from marvin.utilities.vcenter_configs_new import VCENTER_DICT
from tenacity import (
    retry,
    retry_if_result,
    retry_if_exception_type,
    stop_after_delay,
    stop_after_attempt,
    wait_random,
)
from random import sample
from pathlib import Path
import requests
import re
from requests.auth import HTTPBasicAuth
from http.client import RemoteDisconnected
from marvin.utilities.ssh import SSHSession
from marvin.utilities.win_rm import WinRM
import logging
from marvin.jarvis.jarvis_utilities import wait_for_valid_ip

logger = logging.getLogger(__name__)


class VCKeepAlive(threading.Thread):
    def __init__(self, service_instance, event_wait=300):
        super().__init__()
        self.si = service_instance
        self.event = threading.Event()
        self.daemon = True
        self.wait_time = event_wait
        self.name = "{}-{}".format(
            __class__.__name__,
            self.si.content.sessionManager.currentSession.key,
        )

    def run(self):
        """Keep the service instance session alive by touching dynamic data
        every 5 minutes."""
        while not self.event.wait(self.wait_time):
            self.touch_session()
            logger.debug(
                "Retry stats: {}".format(self.touch_session.retry.statistics)
            )

    @retry(
        retry=retry_if_exception_type(RemoteDisconnected),
        reraise=True,
        stop=stop_after_attempt(5),
        wait=wait_random(1, 10),
    )
    def touch_session(self):
        try:
            if self.si.content.sessionManager.currentSession is not None:
                logger.debug(
                    "Service Instance session: {} last active: {}".format(
                        self.si.content.sessionManager.currentSession.key,
                        self.si.content.sessionManager.currentSession.lastActiveTime,
                    )
                )
            else:
                logger.debug("Service Instance session was None.")
        except RemoteDisconnected as disconnected_err:
            logger.exception(
                'Caught {} in keepalive run.'.format(disconnected_err)
            )
            logger.debug(
                'Thread: {} Keep alive event: {}'.format(self, self.event)
            )
            raise


class VCenter:
    """
    Most of this is stolen - errr... Borrowed. Well, inspired by, maybe.
    Nope - stolen from https://github.com/rreubenur/vmware-pyvmomi-examples/

    The basics of VM control. Connect to vCenter, Power control, Snapshot control and lifecycle
    """

    def __init__(self, vcenter='qa-vcenter', idle_timeout=1800):
        """Setup and configure pyvmomi connection to the specified vcenter.

        :param str vcenter: Vcenter to retrieve configuration for.
        :param int idle_timeout: Connection pool timeout for the pyvmomi service instance, default 30 minutes.
        """
        self._config = VCENTER_DICT[
            vcenter.split('.')[0]
        ]  # allow passing of vcenter='qa-vcenter.stc.eng' and still find right config
        self.username = self._config['USERNAME']
        self.password = self._config['PASSWORD']
        self.si = SmartConnectNoSSL(
            host=self._config['VSPHERE_HOST'],
            user=self.username,
            pwd=self.password,
            connectionPoolTimeout=idle_timeout,
        )
        self._vm_names = []
        self._filtered_list = []
        self._ip_address_list = []
        self.cattle = (
            []
        )  # This is a list to keep track of VM's created during the life of this object.
        # Start a thread to keep the session alive.
        self.keepalive = VCKeepAlive(self.si)
        self.keepalive.start()
        atexit.register(self.cleanup)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    def cleanup(self):
        try:
            logger.debug(
                "Disconnecting service instance session: {} to {}".format(
                    str(self.si.content.sessionManager.currentSession),
                    self._config['VSPHERE_HOST'],
                )
            )
        except RemoteDisconnected as disconnected_err:
            logger.exception(
                "Error in vcenter object cleanup: {}".format(disconnected_err)
            )
        Disconnect(self.si)
        logger.debug('Stopping keepalive: {} ...'.format(self.keepalive.name))
        self.keepalive.event.set()
        logger.debug('Cleaned up VCenter object')

    @property
    def vm_name_list(self):
        return self._vm_names

    @property
    def filtered_list(self):
        return self._filtered_list

    @filtered_list.setter
    def filtered_list(self, value):
        self._filtered_list = []
        self._filtered_list = value

    @property
    def ip_address_list(self):
        return self._ip_address_list

    @ip_address_list.setter
    def ip_address_list(self, value):
        self._ip_address_list = []
        self._ip_address_list = value

    def wait_for_task(self, task, raise_on_error=True):
        logger.info(
            f'{task.info.name.info.name} task {task} started at {task.info.startTime}'
        )

        def progress_update(task, percentdone):
            logger.info(
                f'{task.info.name.info.name} task {task} progress is: {percentdone}'
            )

        task_result = WaitForTask(
            task, raiseOnError=raise_on_error, onProgressUpdate=progress_update
        )
        if task_result == vim.TaskInfo.State.success:
            logger.info(
                f"{task.info.name.info.name} task {task} succeeded at {task.info.completeTime}, result: {task.info.result}"
            )
            return task.info.result
        elif task_result == vim.TaskInfo.State.error:
            err_msg = f'{task.info.name.info.name} task {task} failed at {task.info.completeTime}, error: {task.info.error.msg}'
            logger.error(err_msg)
            raise Exception(err_msg)

    def get_all_vms(self, regex_filter=None):
        """Gets the list of VMs from the connected server.

        :return: Container view of the VMs
        """
        content = self.si.RetrieveContent()
        vmview = content.viewManager.CreateContainerView(
            content.rootFolder, [vim.VirtualMachine], True
        ).view
        return (
            vmview
            if not regex_filter
            else [vm for vm in vmview if re.match(regex_filter, vm.name)]
        )

    def get_all_clusters(self):
        """Get the list of Clusters from the connected server.

        :return: Container view of the Clusters
        """
        content = self.si.RetrieveContent()
        return content.viewManager.CreateContainerView(
            content.rootFolder, [vim.ClusterComputeResource], True
        ).view

    def get_all_datacenters(self):
        """Get the list of Datacenters from the connected server.

        :return: Container view of the DCs
        """
        content = self.si.RetrieveContent()
        return content.viewManager.CreateContainerView(
            content.rootFolder, [vim.Datacenter], True
        ).view

    def filter_vm_list(self, item, string):
        """Created a filtered list of VM from the Make_list functions.

        :param item: Container view item that contains your VM list
        :param str string: String to match for filtering
        :return:
        """
        self._filtered_list = []
        for i in self.make_list():
            if string in i[item]:
                self._filtered_list.append(i)
        return self.filtered_list

    def get_ip_address_list(self):
        """Gets the IP address list of all the VMs and adds them to the
        self._ip_address_list.

        :return:
        """
        for i in self.get_all_vms():
            self._ip_address_list.append(i)

    def get_filtered_ip_address_list_by_name(self, vm_name):
        """Filters and then gets the IP address of a VM.

        :param str vm_name: The string you'd like to filter by
        :return: self._ip_address_list
        """
        vm_list = self.filter_vm_list('name', vm_name)
        for i in vm_list:
            print(i)
            self._ip_address_list.append(i['ip_address'])
        return self._ip_address_list

    def make_list(self, get_unclaimed=True, get_claimed=True):
        """Makes a list of VM dicts to be exported into GoogleSheets (or
        other).

        :param bool get_unclaimed: Get unclaimed vms
        :param bool get_claimed: Get claimed vms

        Example VM dict:

            {'name': 'roxanne-director',
             'host': 'qa-vcenter.stc.eng:443',
             'ip_address': '10.30.100.99',
             'power_state': 'ON',
             'last_powered': '2017-12-14',
             'days_since_power': '0004',
             'claim': 'Unclaimed'}
        """
        vmlist = []
        for vm in self.get_all_vms():
            try:
                summary = vm.summary
                vm_dict = {'name': summary.config.name}

                # skip claimed or unclaimed depending on kwargs above
                claimed = False
                if summary.config.annotation is not None:
                    anno = summary.config.annotation
                    if "Claimed by:" in anno:
                        claimed = True
                if not get_claimed:
                    if claimed:
                        continue
                if not get_unclaimed:
                    if not claimed:
                        continue

                # get host
                vm_dict['host'] = vm._stub.host

                # get IP address
                vm_dict['ip_address'] = vm.summary.guest.ipAddress

                # Get Power state
                vm_dict['power_state'] = summary.runtime.powerState
                if summary.runtime.bootTime is not None:
                    timesincelastboot = (
                        datetime.now(pytz.utc) - summary.runtime.bootTime
                    )
                    vm_dict['last_powered'] = str(
                        summary.runtime.bootTime.date()
                    )
                    vm_dict['days'] = timesincelastboot.days
                else:
                    vm_dict['last_powered'] = "NEVER"
                    vm_dict['days'] = "--"

                # Get claimed text
                if claimed:
                    claim_string = "Claimed by: "
                    start = anno.find(claim_string)
                    endline = anno[start:].find('\n')
                    end = endline if endline != -1 else None
                    vm_dict['claim'] = anno[start + len(claim_string) : end]
                else:
                    vm_dict['claim'] = "Unclaimed"

                vmlist.append(vm_dict)
            except vmodl.fault.ManagedObjectNotFound as e:
                logger.exception(
                    "Caught VM not found err in make_list: {}".format(e)
                )
        return vmlist

    def make_name_list(self):
        """Puts the name list into the internal variable self._vm_names.

        :return:
        """
        for vm in self.get_all_vms():
            if vm.summary.config.name:
                self._vm_names.append(vm.summary.config.name)
        return self._vm_names

    def get_vm_by_name(self, name):
        """Gets the VM container view for a VM.

        :param str name: String to use for filtering vms
        :return: container view: Container view fo the selected VM
        """
        for vm in self.get_all_vms():
            try:
                if name == vm.name:
                    logger.debug(f'{vm} matched name {name}')
                    return vm
            except vmodl.fault.ManagedObjectNotFound as mobjerr:
                logger.exception(
                    'Caught {} in get_vm_by_name, vm {} went away.'.format(
                        mobjerr, vm
                    )
                )

    def get_host_by_name(self, host_name):
        for cluster in self.get_all_clusters():
            for host in cluster.host:
                if host.name == host_name:
                    return host
        return None

    @retry(
        retry=retry_if_result(lambda result: result in ["", None]),
        stop=stop_after_delay(300),
        wait=wait_random(max=10),
    )
    def get_vm_hostname_by_ip(self, ip_address):
        """Gets the VM hostName by searching via IP Address.

        :param str ip_address: IP address of the VM
        :return: hostname of the VM
        :rtype: str
        """
        logger.info(f"Attempt to get machine hostname with IP {ip_address}")
        return next(
            (
                machine.summary.guest.hostName
                for machine in self.get_all_vms()
                if ip_address == machine.summary.guest.ipAddress
            ),
            None,
        )

    def get_network_by_hostname(self, host_name):
        """Get the list of network names that are attached to a particular
        host.

        :param str host_name: Name of the host
        :return: list host_network_list: list of all network names attached to a host
        """
        host = self.get_host_by_name(host_name)
        host_network_list = []
        if host:
            host_network_list = [network.name for network in host.network]
        return host_network_list

    def get_datastores_by_hostname(self, host_name):
        """Get the list of datastores attached to a particular host.

        :param str host_name: Name of the host
        :return: list host_datastore_list: list of all datastores attached to a host
        """
        host = self.get_host_by_name(host_name)
        if host:
            return [datastore.name for datastore in host.datastore]
        else:
            raise Exception(
                'The host name: {} is not found.'.format(host_name)
            )

    def get_esxi_version_by_hostname(self, host_name):
        """get ESXI version of a particular host.

        :param str host_name: Name of the host
        :return: str: ESXI version of the host
        """
        host = self.get_host_by_name(host_name)
        if host:
            return host.config.product.version
        else:
            raise Exception(
                'The host name: {} is not found.'.format(host_name)
            )

    def get_ethernet_portgroup_id(self, network_switch) -> str:
        """get the portgroup id of the switch.

        :param str network_switch: Name of the switch
        :return: portgroup id of the switch
        """
        network_key = None
        for dc in self.get_all_datacenters():
            for network in dc.networkFolder.childEntity:
                if network.name == network_switch:
                    if hasattr(network, 'key'):
                        network_key = network.key
                    else:
                        logger.debug(
                            f"{network.name} is not a switch, it doesn't have portgroup id."
                        )
        if not network_key:
            logger.debug(
                'Requested network switch name is not present in VCenter.'
            )
        return network_key

    def get_ethernet_switch_id(self, network_switch) -> str:
        """get the switch id of the switch.

        :param str network_switch: Name of the switch
        :return: switch id of the switch
        """
        switch_id = None
        for dc in self.get_all_datacenters():
            for network in dc.networkFolder.childEntity:
                if network.name == network_switch:
                    if hasattr(network, 'key'):
                        switch_id = (
                            network.config.distributedVirtualSwitch.uuid
                        )
                    else:
                        logger.debug(
                            f"{network.name} is not a switch, it doesn't have switch id."
                        )
        if not switch_id:
            logger.debug(
                'Requested network switch name is not present in VCenter.'
            )
        return switch_id

    def get_ip_by_hostname(self, host_name):
        """Get the ip(s) of a particular host.

        :param str host_name: Name of the host
        :return: list host_ip_list : ip(s) of the host
        """
        host = self.get_host_by_name(host_name)
        if host:
            return [
                vnic.spec.ip.ipAddress for vnic in host.config.network.vnic
            ]
        else:
            raise Exception(
                'The host name: {} is not found.'.format(host_name)
            )

    def get_overall_status_by_hostname(self, host_name):
        """Get overall status of a particular host.

        :param str host_name: Name of the host
        :return: Overall status of host
        :rtype: str
        :raises: Exception
        """
        host = self.get_host_by_name(host_name)
        if host:
            return host.overallStatus
        else:
            raise Exception(
                'The host name: {} is not found.'.format(host_name)
            )

    def get_vm_name_by_ip(self, ip_address):
        """Gets the VM Name by searching via IP Address.

        :param str ip_address: String to use for filtering vms
        :return: container view: Container view fo the selected VM
        """
        return next(
            (
                machine.name
                for machine in self.get_all_vms()
                if ip_address == machine.summary.guest.ipAddress
            ),
            None,
        )

    def get_cluster_by_name(self, name):
        """Find a cluster by it's name and return it.

        :return: pyVmomi.VmomiSupport.vim.ClusterComputeResource cluster
        """
        return next(
            (
                cluster
                for cluster in self.get_all_clusters()
                if name in cluster.name
            ),
            None,
        )

    def get_all_clusters_hosts(self, cluster_name):
        host_list = []
        for cluster in self.get_all_clusters():
            if cluster.name == cluster_name:
                for host in cluster.host:
                    host_list.append(host.name)
        return host_list

    def get_all_hosts(self):
        """Get the list of hosts present in vcenter.

        :return: dict host_dict: dict with the cluster names as keys and the hosts in lists under those keys
        """
        host_dict = {}
        for cluster in self.get_all_clusters():
            host_dict[cluster.name] = [host.name for host in cluster.host]
        return host_dict

    def get_all_healthy_hosts(self):
        host_list = []
        for cluster in self.get_all_clusters():
            for host in cluster.host:
                if host.overallStatus != "red":
                    host_list.append(host.name)
        return host_list

    def get_vm_names_by_cluster(self, cluster_name):
        """Returns a list of all vms located in a specified cluster.

        :param str cluster_name: The name of the cluster you want to know the vms of.
        :return: list
        """
        vm_name_list = []
        content = self.si.RetrieveContent()
        for dc in content.rootFolder.childEntity:
            for cluster in dc.hostFolder.childEntity:
                if cluster.name == cluster_name:
                    for host in cluster.host:
                        for vm in host.vm:
                            vm_name_list.append(vm.summary.config.name)
        return vm_name_list

    def delete_vm_by_name(self, vm_name):
        """Selects a VM by explicit name and then deletes it.

        :param str vm_name: Name of the VM to delete
        """
        vm = self.get_vm_by_name(vm_name)
        if vm is not None:
            if (
                vm.runtime.powerState == "poweredOn"
                or vm.runtime.powerState == "suspended"
            ):
                logger.info(f'VM {vm_name} is powering off')
                self.wait_for_task(vm.PowerOffVM_Task())
            logger.info(f'VM {vm_name} is going away forever')
            self.wait_for_task(vm.Destroy_Task())
            if vm_name in self.cattle:
                self.cattle.remove(vm_name)

    def delete_vm_list(self, vm_list):
        """Deletes a list of VMs when passed a list of names. This allows us to
        use Pool() to multiprocess.

        :param list vm_list: List of VM Names to be deleted
        :return:
        """
        pool = Pool(10)
        c = pool.map(self.delete_vm_by_name, vm_list)
        pool.close()
        pool.join()

    def delete_all_vm_by_string(self, regex):
        """Combo Function to filter out a list of VMs bas3ed on a filter string
        and then delete them by passing to the delete_vm_list method.

        :param str regex: String to filter the list by
        :return:
        """
        list_to_delete = []

        for vm in self.make_list():
            if re.match(regex, vm['name']):
                list_to_delete.append(vm['name'])
                logger.info('VM {} is being deleted'.format(vm['name']))
        self.delete_vm_list(list_to_delete)

    def power_suspend_vm(self, vm_name):
        """Suspends a VM by the string name of the VM.

        :param str vm_name: VM Name
        """
        vm = self.get_vm_by_name(vm_name)
        if vm.runtime.powerState == 'poweredOn':
            self.wait_for_task(vm.SuspendVM_Task())
            logger.info(f'VM {vm_name} is suspending')
        else:
            logger.info(
                f'VM {vm_name} is at power state: {vm.runtime.powerState}'
            )

    def power_suspend_vm_list(self, vm_list):
        """Suspends a list of VMs.

        :param list vm_list: list of VM Names to be suspended. This uses Pool() for multiprocessing
        """
        pool = Pool(10)
        pool.map(self.power_suspend_vm, vm_list)
        pool.close()
        pool.join()

    def power_off_vm(self, vm_name):
        """Powers off a VM by the string name of the VM.

        :param str vm_name: VM Name
        """
        vm = self.get_vm_by_name(vm_name)
        if vm.runtime.powerState == "poweredOn":
            logger.info(f'VM {vm_name} is powering off')
            self.wait_for_task(vm.PowerOffVM_Task())
        else:
            logger.info(f'VM {vm_name} is already powered off')

    def power_off_vm_list(self, vm_list):
        """Powers off a list of VMs.

        :param list vm_list: list of VM Names to be turned off. This uses Pool() for multiprocessing
        """
        pool = Pool(10)
        c = pool.map(self.power_off_vm, vm_list)
        pool.close()
        pool.join()

    def power_off_all_vm_by_string(self, vm_filter):
        """Combo Function that filters a list of VM by name and then powers
        them off by sending the list to the power_off_vm_by_list method.

        :param str vm_filter: String to filter list by
        """
        self.power_off_vm_list(
            [i['name'] for i in self.make_list() if vm_filter in i['name']]
        )

    def power_on_vm(self, vm_name):
        """Does what it says on the tin. Powers on a VM when passed a VM Name.

        :param str vm_name: VM Name
        """
        vm = self.get_vm_by_name(vm_name)
        if vm.runtime.powerState != "poweredOn":
            self.wait_for_task(vm.PowerOnVM_Task())
        else:
            logger.info(f'VM {vm_name} is already powered on')

    def power_on_vm_list(self, vm_list):
        """Uses Pool() to power on a list of VMs.

        :param list vm_list: A list of VMs to power on
        """
        pool = Pool(10)
        c = pool.map(self.power_on_vm, vm_list)
        pool.close()
        pool.join()

    def power_on_all_vm_by_string(self, vm_filter):
        """Combo function that filters and then powers on VMs.

        :param str vm_filter: String to filter the VM list by
        """
        self.power_on_vm_list(
            [i['name'] for i in self.make_list() if vm_filter in i['name']]
        )

    def power_on_some_vm_by_string(self, vm_filter, percentage):
        """Intended to power on a percentage of the overall VMs you find
        through a filtered list.

        :param str vm_filter: String to use for filtering the list of VMs that are returned
        :param int percentage: a percentage of machines to power on
        """
        decimal = percentage / 100
        working_list = []
        list_to_power_on = []
        for i in self.make_list():
            if vm_filter in i['name'] and i['power_state'] != 'poweredOn':
                working_list.append(i['name'])
        if len(working_list) > 0:
            number_to_iterate = int(len(working_list) * decimal)
            for i in range(number_to_iterate):
                list_to_power_on.append(working_list[i])
        self.power_on_vm_list(list_to_power_on)

    def power_off_some_vm_by_string(self, vm_filter, percentage):
        """Intended to power on a percentage of the overall VMs you find
        through a filtered list.

        :param str vm_filter: String to use for filtering the list of VMs that are returned
        :param int percentage: a percentage of machines to power on
        """
        decimal = percentage / 100
        working_list = []
        list_to_power_off = []
        for vm in self.make_list():
            if vm_filter in vm['name'] and vm['power_state'] != 'poweredOff':
                working_list.append(vm['name'])
        if len(working_list) > 0:
            number_to_iterate = int(len(working_list) * decimal)
            for i in range(number_to_iterate):
                list_to_power_off.append(working_list[i])
        self.power_off_vm_list(list_to_power_off)

    def reset_vm(self, vm_name):
        """Selects a VM by explicit name and then restart its guest OS.

        :param str vm_name: Name of the VM to delete
        """
        vm = self.get_vm_by_name(vm_name)
        self.wait_for_task(vm.ResetVM_Task())

    def reboot_guest_os(self, vm_name):
        vm = self.get_vm_by_name(vm_name)
        try:
            self.wait_for_task(vm.RebootGuest())
        except:
            self.wait_for_task(vm.ResetVM_Task())

    @retry(
        retry=retry_if_result(lambda result: result is None),
        stop=stop_after_delay(300),
        wait=wait_random(max=10),
    )
    def get_vm_ip(self, vm_name):
        """Get's the IP address of a machine by name.

        :param str vm_name: VM Name to get IP address for

        :return: Guest IP or None
        """
        vm = self.get_vm_by_name(vm_name)
        if vm.runtime.powerState == 'poweredOn':
            return vm.summary.guest.ipAddress
        else:
            raise Exception("VM is not powered on, no IP address to retrieve!")

    def take_snapshot(
        self, vm, snap_name=None, desc=None, memory=True, quiesce=False
    ):
        """Creates the snapshot of the given VM with the given snapshot name.

        :param str vm: Name or IP or Hostname of the VM
        :param str snap_name: Name given to the Snapshot
        :param str desc: Description of the Snapshot
        :param bool memory: To capture the memory state in the snapshot
        :param bool quiesce: To quiesce the snapshot
        :return: Name of the snapshot
        :rtype: str
        """
        vm_obj = next(
            (
                machine.summary.vm
                for machine in self.get_all_vms()
                if vm
                in [
                    machine.summary.guest.ipAddress,
                    machine.summary.guest.hostName,
                    machine.summary.vm.name,
                ]
            ),
            None,
        )
        snap_name = (
            snap_name if snap_name else 'TestSnapshot_' + str(datetime.now())
        )
        self.wait_for_task(
            vm_obj.CreateSnapshot_Task(
                name=snap_name,
                description=desc,
                memory=memory,
                quiesce=quiesce,
            )
        )
        return snap_name

    def get_snapshots(self, rootlist):
        """Starting from the root list, returns a list of snapshot objects.

        :param rootlist: the VM snapshot rootlist
        :return: list of snapshot objects
        """
        results = []
        for s in rootlist:
            results.append(s)
            results += self.get_snapshots(s.childSnapshotList)
        return results

    def find_matching_snapshot(self, vm_name, snap_name):
        """Finds the snapshot object that matches the given string.

        :param str vm_name: Name of the VM
        :param str snap_name: Name of the snapshot to be found
        :return: Snapshot object
        """
        vm_obj = self.get_vm_by_name(vm_name)
        snapshots = self.get_snapshots(vm_obj.snapshot.rootSnapshotList)
        if len(snapshots) < 1:
            return None
        return next(s for s in snapshots if snap_name in s.name)

    def revert_to_snapshot(self, vm, snap_name=None):
        """Reverts the snapshot to the latest snapshot if snapshot name is not
        provided.

        :param str vm: Name or IP or Hostname of the vm
        :param str snap_name: Name of the snapshot to do revert with
        :return: None
        """
        vm_obj = next(
            (
                machine.summary.vm
                for machine in self.get_all_vms()
                if vm
                in [
                    machine.summary.guest.ipAddress,
                    machine.summary.guest.hostName,
                    machine.summary.vm.name,
                ]
            ),
            None,
        )

        if snap_name:
            snapshot = self.find_matching_snapshot(vm_obj.name, snap_name)
            WaitForTask(snapshot.snapshot.RevertToSnapshot_Task())
        else:
            self.wait_for_task(
                vm_obj.RevertToCurrentSnapshot_Task(
                    vm_obj.summary.runtime.host
                )
            )

    def get_all_snapshots_by_string(self, string):
        list_to_retrieve = []
        for i in self.make_list():
            if string in i['name']:
                list_to_retrieve.append(i['name'])
        for vm in list_to_retrieve:
            self.get_snapshots(vm)

    def delete_all_snapshots_by_machine_name(self, vm_or_name):
        cleanup_vm = (
            vm_or_name
            if isinstance(vm_or_name, vim.VirtualMachine)
            else self.get_vm_by_name(vm_or_name)
        )
        if cleanup_vm.snapshot:
            logger.info(f'Deleting snapshots for vm: {cleanup_vm.name}')
            return self.wait_for_task(cleanup_vm.RemoveAllSnapshots_Task())

    def delete_all_snapshots_by_list(self, vm_list):
        pool = Pool(10)
        c = pool.map(self.delete_all_snapshots_by_machine_name, vm_list)
        pool.close()
        pool.join()

    def consolidate_disks_by_machine_name(self, vm_or_name):
        cleanup_vm = (
            vm_or_name
            if isinstance(vm_or_name, vim.VirtualMachine)
            else self.get_vm_by_name(vm_or_name)
        )
        if cleanup_vm.summary.runtime.consolidationNeeded:
            logger.info(f'Consolidating disks for vm: {cleanup_vm.name}')
            return self.wait_for_task(cleanup_vm.ConsolidateVMDisks_Task())

    def consolidate_all_disks_by_list(self, vm_list):
        pool = Pool(10)
        c = pool.map(self.consolidate_disks_by_machine_name, vm_list)
        pool.close()
        pool.join()

    def delete_all_snapshots_by_string(self, snap_filter):
        """Deletes all snapshots by filter string.

        :param str snap_filter: String to filter snapshots with
        :return: None
        """
        self.delete_all_snapshots_by_list(
            [i['name'] for i in self.make_list() if snap_filter in i['name']]
        )

    def get_vm_disks_size(self, vm_name):
        test_vm = self.get_vm_by_name(vm_name)
        return [
            device.deviceInfo.summary
            for device in test_vm.config.hardware.device
            if type(device).__name__ == 'vim.vm.device.VirtualDisk'
        ]

    def vm_total_disk_space(self, vm_name):
        return sum(
            [
                int(i.split(" ")[0].replace(",", ""))
                for i in self.get_vm_disks_size(vm_name)
            ]
        )

    def clone_vm(
        self,
        source_vm_name,
        target_vm_name,
        cluster=None,
        target_datastore=None,
        template=False,
    ):
        source_vm = self.get_vm_by_name(source_vm_name)
        if template is True:
            if cluster is not None:
                cluster = self.get_cluster_by_name(cluster)
                target_datastore = (
                    source_vm.datastore[0]
                    if not target_datastore
                    else next(
                        (
                            ds
                            for ds in cluster.datastore
                            if ds.name == target_datastore
                        )
                    )
                )
                relocate_spec = vim.vm.RelocateSpec(
                    pool=cluster.resourcePool, datastore=target_datastore
                )
            else:
                raise Exception(
                    "For cloning a template to VM, cluster name should be provided."
                )
        else:
            relocate_spec = vim.vm.RelocateSpec(
                pool=source_vm.resourcePool, datastore=source_vm.datastore[0]
            )
        cloneSpec = vim.vm.CloneSpec(
            powerOn=True, template=False, location=relocate_spec
        )
        logger.info(
            "Cloning {} to {}...".format(source_vm_name, target_vm_name)
        )
        task = source_vm.Clone(
            name=target_vm_name, folder=source_vm.parent, spec=cloneSpec
        )
        task_result = self.wait_for_task(task)
        logger.debug("Task completed")
        logger.debug("Task info:{}".format(task_result))
        self.cattle.append(target_vm_name)  # add this to list of session vms.
        return task_result

    def get_vm_data(self, vm, depth=1):
        """Print information for a particular virtual machine or recurse into a
        folder with depth protection."""
        maxdepth = 10
        data = {}

        # if this is a group it will have children. if it does, recurse into them
        # and then return
        if hasattr(vm, 'childEntity'):
            if depth > maxdepth:
                return
            vmList = vm.childEntity
            for c in vmList:
                self.get_vm_data(c, depth + 1)
            return

        data[vm.summary.config.name] = {
            'name': vm.summary.config.name,
            'vmPathName': vm.summary.config.vmPathName,
            'guestFullName': vm.summary.config.guestFullName,
            'powerState': vm.summary.runtime.powerState,
            'ip': vm.summary.guest.ipAddress,
            'host': vm.summary.runtime.host.name,
            'datastore': [datastore.name for datastore in vm.datastore],
            'annotation': vm.summary.config.annotation,
        }
        logger.info("Data in GetVMData:{}".format(data))
        return data

    def add_virtual_disk(
        self, vm_name, disk_size, disk_type='thin', disk_mode='persistent'
    ):
        test_vm = self.get_vm_by_name(vm_name)
        spec = vim.vm.ConfigSpec()
        # get all disks on a VM, set unit_number to the next available
        unit_number = 0
        for dev in test_vm.config.hardware.device:
            if hasattr(dev.backing, 'fileName'):
                unit_number = int(dev.unitNumber) + 1
                # unit_number 7 reserved for scsi controller
                if unit_number == 7:
                    unit_number += 1
                if unit_number >= 16:
                    raise Exception("we don't support this many disks")
            if isinstance(dev, vim.vm.device.VirtualSCSIController):
                controller = dev
        # add disk here
        dev_changes = []
        new_disk_kb = int(disk_size) * 1024 * 1024
        disk_spec = vim.vm.device.VirtualDeviceSpec()
        disk_spec.fileOperation = "create"
        disk_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        disk_spec.device = vim.vm.device.VirtualDisk()
        disk_spec.device.backing = (
            vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
        )
        if disk_type == 'thin':
            disk_spec.device.backing.thinProvisioned = True
        disk_spec.device.backing.diskMode = disk_mode
        disk_spec.device.unitNumber = unit_number
        disk_spec.device.capacityInKB = new_disk_kb
        disk_spec.device.controllerKey = controller.key
        dev_changes.append(disk_spec)
        spec.deviceChange = dev_changes
        TASK = test_vm.ReconfigVM_Task(spec=spec)
        self.wait_for_task(TASK)
        if TASK.info.state != 'success':
            raise Exception(
                'Add virtual disk operation to VM::{} failed'.format(vm_name)
            )

    def delete_virtual_disk(self, vm_name, disk_number):
        vm_obj = self.get_vm_by_name(vm_name)
        hdd_label = 'Hard disk ' + str(disk_number)
        virtual_hdd_device = None
        for dev in vm_obj.config.hardware.device:
            if (
                isinstance(dev, vim.vm.device.VirtualDisk)
                and dev.deviceInfo.label == hdd_label
            ):
                virtual_hdd_device = dev
        if not virtual_hdd_device:
            raise Exception(
                'Virtual {} could not be found.'.format(virtual_hdd_device)
            )
        virtual_hdd_spec = vim.vm.device.VirtualDeviceSpec()
        virtual_hdd_spec.operation = (
            vim.vm.device.VirtualDeviceSpec.Operation.remove
        )
        virtual_hdd_spec.device = virtual_hdd_device
        spec = vim.vm.ConfigSpec()
        spec.deviceChange = [virtual_hdd_spec]
        TASK = vm_obj.ReconfigVM_Task(spec=spec)
        self.wait_for_task(TASK)
        if TASK.info.state != 'success':
            raise Exception(
                'Delete virtual disk operation from VM::{} failed'.format(
                    vm_name
                )
            )

    def upload_floppy_image(
        self,
        local_image_path,
        datacenter="4th Floor",
        datastore="vSanDatastore",
        remote_folder="automation/floppy_images",
    ):
        """Upload a floppy image suitable for jarvis deploy.

        :param str local_image_path: Path to local image.
        :param str datacenter: ESX datacenter to use
        :param str datastore: ESX datastore to use
        :param str remote_folder: Folder on the ESX datastore to place the image in.
        :return: Full "[datastore] path/to/image.img" string.
        """
        auth = HTTPBasicAuth(self.username, self.password)
        params = {'dsName': datastore, 'dcPath': datacenter}
        img_path = Path(local_image_path)

        with open(img_path, 'rb') as image_file:
            image_data = image_file.read()
            url = 'https://{}/folder/{}/{}'.format(
                self._config['VSPHERE_HOST'], remote_folder, img_path.name
            )
            logger.info(
                'PUTing {} to {} in datastore: {}'.format(
                    img_path, url, datastore
                )
            )
            r = requests.put(
                url,
                auth=auth,
                data=image_data,
                timeout=30,
                params=params,
                verify=False,
            )
            r.raise_for_status()

        return f'[{datastore}] {remote_folder}/{img_path.name}'

    def delete_floppy_image(
        self,
        remote_image_file,
        datacenter="4th Floor",
        datastore="vSanDatastore",
        remote_folder="automation/floppy_images",
    ):
        """Upload a floppy image suitable for jarvis deploy.

        :param str remote_image_file: Path to image in ESX datastore.
        :param str datacenter: ESX datacenter to use
        :param str datastore: ESX datastore to use
        :param str remote_folder: Folder on the ESX datastore to delete file from.
        :return: None.
        """
        auth = HTTPBasicAuth(self.username, self.password)
        params = {'dsName': datastore, 'dcPath': datacenter}
        url = 'https://{}/folder/{}/{}'.format(
            self._config['VSPHERE_HOST'], remote_folder, remote_image_file
        )
        logger.info('DELETEing {} from datastore: {}'.format(url, datastore))
        r = requests.delete(
            url, auth=auth, timeout=30, params=params, verify=False
        )
        r.raise_for_status()

    def attach_virtual_floppy(self, vm_name, floppy_path):
        """Attaches a floppy device backed by an image to a vm.

        :param str vm_name: Name of vm to attach floppy to
        :param str floppy_path: Path to floppy image. See format from upload_floppy_image return.
        :return:
        """
        vm = self.get_vm_by_name(vm_name)
        controller = None
        floppy_device_key = 8000  # 800x reserved for floppies
        # Find Super I/O controller and free device key
        for device in vm.config.hardware.device:
            if isinstance(device, vim.vm.device.VirtualSIOController):
                controller = device
            if isinstance(device, vim.vm.device.VirtualFloppy):
                floppy_device_key = int(device.key) + 1

        floppyspec = vim.vm.device.VirtualDeviceSpec()
        floppyspec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        floppyspec.device = vim.vm.device.VirtualFloppy(
            deviceInfo=vim.Description(
                label='Floppy drive 1', summary='Remote device'
            )
        )
        floppyspec.device.key = floppy_device_key
        floppyspec.device.controllerKey = controller.key
        logger.info(
            f'Attaching floppy to vm: {vm_name} backed by: {floppy_path}'
        )

        floppyspec.device.backing = vim.vm.device.VirtualFloppy.ImageBackingInfo(
            fileName=floppy_path
        )
        floppyspec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo(
            startConnected=True,
            allowGuestControl=True,
            connected=True,
            status='untried',
        )
        config_spec = vim.vm.ConfigSpec(deviceChange=[floppyspec])
        self.wait_for_task(vm.ReconfigVM_Task(spec=config_spec))

    def vm_migration(
        self, vm_name, destination_host=None, vmotion=False, svmotion=False
    ):
        """Migrates a VM to a specified host or to another datastore on same
        host or to another host under the same cluster Amongst the parameters
        destination_host, vmotion and svmotion only one is required at a time.

        :param str vm_name: Name of the VM which is to be migrated
        :param str destination_host: Name of host to which VM will be migrated
        :param bool vmotion: Set True to perform vmotion
        :param bool svmotion: Set True to perform svmotion
        :return: Name of the destination host
        """
        vm = self.get_vm_by_name(vm_name)
        vm_relocate_spec = vim.vm.RelocateSpec()
        # Live Migration :: Change both host and datastore
        if destination_host is not None:
            if self.get_host_by_name(destination_host) is None:
                raise Exception(
                    "No valid host found with name : {}".format(
                        destination_host
                    )
                )
            target_host = self.get_host_by_name(destination_host)
            vm_relocate_spec.host = target_host
            vm_relocate_spec.pool = target_host.parent.resourcePool
            datastores = target_host.datastore
            for datastore in datastores:
                if datastore.overallStatus != 'red':
                    vm_relocate_spec.datastore = datastore
                    break
            if vm_relocate_spec.datastore is None:
                raise Exception(
                    "No datastore in healthy state for this operation"
                )
        # Migrating to another datastore within the same host
        elif svmotion:
            vm_relocate_spec.host = vm.runtime.host
            vm_relocate_spec.pool = vm.resourcePool
            datastores = vm.runtime.host.datastore
            for datastore in datastores:
                if (
                    datastore.overallStatus != 'red'
                    and datastore != vm.datastore[0]
                ):
                    vm_relocate_spec.datastore = datastore
                    break
            if vm_relocate_spec.datastore is None:
                raise Exception("No datastore found for this operation")
        # Migrating to a host within same cluster
        elif vmotion:
            if vm.runtime.powerState != 'poweredOn':
                raise Exception("vMotion is only for Powered on VMs")
            for host in vm.resourcePool.parent.host:
                if (
                    host != vm.runtime.host
                    and vm.datastore[0] in host.datastore
                ):
                    vm_relocate_spec.host = host
                    break
            if vm_relocate_spec.host is None:
                raise Exception("No host found for this operation")
            vm_relocate_spec.pool = vm.resourcePool
            vm_relocate_spec.datastore = vm.datastore[0]
        self.wait_for_task(vm.Relocate(spec=vm_relocate_spec))
        return vm_relocate_spec.host.name

    def change_ctkenabled(self, vm_name, ctk_val):
        """modifies the ctKEnabled values in ExtraConfig of the vm.

        :param str vm_name: Name of vm
        :param str ctk_val: The new value to be assigned
        :return:
        """
        vm = self.get_vm_by_name(vm_name)
        spec = vim.vm.ConfigSpec()
        opt = vim.option.OptionValue()
        spec.extraConfig = []
        for i in vm.config.extraConfig:
            if "ctkEnabled" in i.key:
                opt.key = i.key
                opt.value = ctk_val
                spec.extraConfig.append(opt)
        self.wait_for_task(vm.ReconfigVM_Task(spec=spec))

    def get_vm_folders(self, datacenter=None) -> dict:
        """Get the vm folders of datacenters in a vcenter.

        :param str datacenter: Name of specific datacenter to retrieve, otherwise get all.
        :return: dict with datacenter name as the key and a list of vm folders in the corresponding datacenter
        """
        folder_dict = {}
        for dc in self.get_all_datacenters():
            folder_dict[dc.name] = [
                obj.name
                for obj in dc.vmFolder.childEntity
                if isinstance(obj, vim.Folder)
            ]
        if datacenter in folder_dict:
            return {datacenter: folder_dict[datacenter]}
        return folder_dict

    def get_vc_version(self) -> str:
        """get the vcenter version.

        :return: version of the vcenter
        """
        return self.si.content.about.version

    def put_clusters_host_in_maintenance_mode(self, cluster_name, timeout=300):
        """Put all the hosts of a cluster into maintenance mode.

        :param str cluster_name:  Name of the Cluster. e.g QA_VAIO
        :param int timeout: Timeout in putting the host in maintenance mode
        :return: None
        """
        cluster = self.get_cluster_by_name(cluster_name)
        vm_list = self.get_vm_names_by_cluster(cluster_name)
        self.power_off_vm_list(vm_list)
        for host in cluster.host:
            if not host.runtime.inMaintenanceMode:
                self.wait_for_task(host.EnterMaintenanceMode_Task(timeout))

    def cluster_exit_maintenance_mode(self, cluster_name, timeout=300):
        """Take all the hosts of a cluster out of maintenance mode.

        :param str cluster_name: Name of the Cluster. e.g QA_VAIO
        :param int timeout: Timeout in exiting the host from maintenance mode
        :return: None
        """
        cluster = self.get_cluster_by_name(cluster_name)
        for host in cluster.host:
            if host.runtime.inMaintenanceMode:
                self.wait_for_task(host.ExitMaintenanceMode_Task(timeout))

    def install_io_filter(self, cluster_name, vib_url, signed=True):
        """Installs IO filter on Cluster.

        :param str cluster_name: Name of the Cluster. e.g QA_VAIO
        :param str vib_url: VIB url
        :param bool signed: Identifies if the filter is signed
        :return: None
        :raises: Exception if any error occurred during the installation of filter
        """
        cluster = self.get_cluster_by_name(cluster_name)
        for host in cluster.host:
            if signed:
                host.configManager.imageConfigManager.UpdateHostImageAcceptanceLevel(
                    "vmware_accepted"
                )
            else:
                host.configManager.imageConfigManager.UpdateHostImageAcceptanceLevel(
                    "community"
                )
        try:
            self.put_clusters_host_in_maintenance_mode(cluster_name)
            self.wait_for_task(
                self.si.content.ioFilterManager.InstallIoFilter_Task(
                    vibUrl=vib_url, compRes=cluster
                )
            )
        except Exception as e:
            logger.exception(
                f"Exception: {e} occurred during installation of IO filter"
            )
            raise e
        finally:
            self.cluster_exit_maintenance_mode(cluster_name)

    def query_io_filter(self, cluster_name, filter_name="staxafe"):
        """This will query the filter string on a given cluster and provides
        the filter id.

        :param str cluster_name: Name of the Cluster. e.g QA_VAIO
        :param str filter_name: Name of the filter. e.g staxafe or stastcesxi
        :return: Filter id of the IO filter
        :rtype: str
        """
        filter_list = self.si.content.ioFilterManager.QueryIoFilterInfo(
            self.get_cluster_by_name(cluster_name)
        )
        return next(
            (fltr.id for fltr in filter_list if filter_name in fltr.id), None
        )

    def query_vms_using_filter(self, cluster_name, filter_name="staxafe"):
        """This will query the VMS using given filter.

        :param str cluster_name: Name of the Cluster. e.g QA_VAIO
        :param str filter_name: Name of the filter e.g staxafe or stastcesxi
        :return: list of VMs using filter
        :rtype: list
        """
        filter_id = self.query_io_filter(cluster_name, filter_name)
        if filter_id:
            vm_list = []
            disks = self.si.content.ioFilterManager.QueryDisksUsingFilter(
                filterId=filter_id,
                compRes=self.get_cluster_by_name(cluster_name),
            )
            for disk in disks:
                vm_list.append(disk.vm.name)
            return list(set(vm_list))
        return None

    def uninstall_io_filter(self, cluster_name, filter_name="staxafe"):
        """Uninstalls the Filter with a given filter string.

        :param str cluster_name: Name of the Cluster. e.g QA_VAIO
        :param str filter_name: Name of the filter. e.g staxafe or stastcesxi
        :return: None
        :raises: Exception if fails to uninstall filter or resolves installation issues on Cluster
        """
        filter_id = self.query_io_filter(cluster_name, filter_name)
        if filter_id:
            vm_list = self.query_vms_using_filter(cluster_name, filter_name)
            self.delete_vm_list(vm_list)
            self.put_clusters_host_in_maintenance_mode(cluster_name)
            try:
                cluster = self.get_cluster_by_name(cluster_name)
                self.wait_for_task(
                    self.si.content.ioFilterManager.UninstallIoFilter_Task(
                        filterId=filter_id, compRes=cluster
                    )
                )
            except Exception:
                # JAR-7271, to resolve uninstallation error, removing filter from host.
                ssh_command = f"esxcli software vib remove -n {filter_name}"
                for host in cluster.host:
                    host_name = host.name
                    retval, std_out, std_err = self.run_cli_command(
                        host_name, ssh_command
                    )
                    if retval == 0:
                        self.wait_for_task(
                            self.si.content.ioFilterManager.ResolveInstallationErrorsOnHost_Task(
                                filterId=filter_id, host=host
                            )
                        )
                    else:
                        raise
            finally:
                self.cluster_exit_maintenance_mode(cluster_name)
        else:
            logger.exception(
                f"No filter with name: '{filter_name}' installed on cluster: {cluster_name}"
            )
            raise Exception(
                f"No filter with name: '{filter_name}' installed on cluster: {cluster_name}"
            )

    def run_cli_command(self, host_name, command):
        """Runs command on esx host cli.

        :param str host_name: Name of the host e.g. r8u32.stc.eng
        :param str command: Command to run on esx host cli
        :return: Returns the return value, standard output and standard error
        :rtype: int, str, str
        """
        host_alias = host_name.split('.')[0]
        for vc in VCENTER_DICT.values():
            if host_alias in vc['HOSTS']:
                host_user = vc['HOSTS'][host_alias]['SSH_USER']
                host_pass = vc['HOSTS'][host_alias]['SSH_PASS']
        with SSHSession(
            hostname=host_name, username=host_user, password=host_pass
        ) as ssh:
            retval, std_out, std_err = ssh.context_execute(command)
        return retval, std_out, std_err

    def get_vm_nics(self, vm):
        vm_obj = (
            vm
            if isinstance(vm, vim.VirtualMachine)
            else self.get_vm_by_name(vm)
        )
        return [
            dev
            for dev in vm_obj.config.hardware.device
            if isinstance(dev, vim.vm.device.VirtualEthernetCard)
        ]

    def change_vm_nic_state(self, vm, nic_number, new_nic_state='connect'):
        """Change the state of a vm's NIC. Stolen shamelessly from:
        https://github.com/vmware/pyvmomi-community-
        samples/blob/master/samples/change_vm_nic_state.py.

        :param str vm: Name of the vm to alter
        :param int nic_number: NIC number to alter
        :param str new_nic_state: State to place the nic in, either connect or disconnect
        :return:
        """
        vm_obj = (
            vm
            if isinstance(vm, vim.VirtualMachine)
            else self.get_vm_by_name(vm)
        )
        nic_prefix_label = 'Network adapter '
        nic_label = nic_prefix_label + str(nic_number)
        for dev in vm_obj.config.hardware.device:
            if (
                isinstance(dev, vim.vm.device.VirtualEthernetCard)
                and dev.deviceInfo.label == nic_label
            ):
                virtual_nic_device = dev
                break
        else:
            raise RuntimeError(
                'Virtual {} could not be found.'.format(nic_label)
            )

        virtual_nic_spec = vim.vm.device.VirtualDeviceSpec()
        virtual_nic_spec.operation = (
            vim.vm.device.VirtualDeviceSpec.Operation.edit
        )
        virtual_nic_spec.device = virtual_nic_device
        virtual_nic_spec.device.key = virtual_nic_device.key
        virtual_nic_spec.device.macAddress = virtual_nic_device.macAddress
        virtual_nic_spec.device.backing = virtual_nic_device.backing
        virtual_nic_spec.device.wakeOnLanEnabled = (
            virtual_nic_device.wakeOnLanEnabled
        )
        connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        if new_nic_state == 'connect':
            connectable.connected = True
            connectable.startConnected = True
        elif new_nic_state == 'disconnect':
            connectable.connected = False
            connectable.startConnected = False
        else:
            connectable = virtual_nic_device.connectable
        virtual_nic_spec.device.connectable = connectable
        spec = vim.vm.ConfigSpec()
        spec.deviceChange = [virtual_nic_spec]
        return self.wait_for_task(vm_obj.ReconfigVM_Task(spec=spec))

    def get_esxi_hostname_by_vm(self, vm):
        """Gets the ESXI Host Name by searching via VM IP Address or hostname.

        :param str vm: String to use for filtering vms, input would be either vm hostname or IP.
        :return: Hostname of containing esx host for vm
        :rtype: str
        """
        return next(
            (
                machine.summary.runtime.host.name
                for machine in self.get_all_vms()
                if vm
                in [
                    machine.summary.guest.ipAddress,
                    machine.summary.guest.hostName,
                ]
            ),
            None,
        )

    def get_vms_by_host(self, hostname):
        """Get all the VM objects from a particular ESX host."""
        esx_host = self.get_host_by_name(hostname)
        return esx_host.vm if esx_host else None

    def add_vm_vmgroup(self, group_name, vm_name, cluster_name):
        """Add a vm to a host affinity group.

        :param str group_name: The name of the host group you want to add the vm to.
        :param str vm_name: The name of the vm you would like added to the host group.
        :param str cluster_name: The name of the cluster that the host group resides on.
        :return: Nothing
        """
        cluster = self.get_cluster_by_name(cluster_name)
        vm = self.get_vm_by_name(vm_name)

        for group in cluster.configurationEx.group:
            if group.name == group_name:
                group.vm.append(vm)
                spec = vim.cluster.ConfigSpecEx(
                    groupSpec=[vim.cluster.GroupSpec(info=group)]
                )
                WaitForTask(cluster.ReconfigureEx(spec=spec, modify=True))
                break
            else:
                raise Exception("Failed to find group %s" % group_name)

    def random_vms_by_host(self, hostname='r3u35.stc.eng'):
        vms_by_host = [
            vm
            for vm in self.get_vms_by_host(hostname)
            if 'qaacattle' in vm.name
        ]
        return sample(vms_by_host, int(len(vms_by_host) / 3))

    def filter_ip_list(self, ip_list: list):
        ipv4s = []
        for ip in ip_list:
            try:
                ipaddress.IPv4Address(ip)
                ipv4s.append(ip)
            except ipaddress.AddressValueError:
                continue
        return ipv4s

    def vm_os_list(self, hostname='r3u35.stc.eng'):
        linuxvm = []
        winvm = []
        for vm in self.random_vms_by_host(hostname):
            vmip = vm.summary.guest.ipAddress
            if vmip is not None:
                linuxvm.append(
                    vmip
                ) if vm.summary.config.guestId != 'windows8Server64Guest' else winvm.append(
                    vmip
                )
        return self.filter_ip_list(linuxvm), self.filter_ip_list(winvm)

    def stress_windows_vm(self, ip_address):
        conn = WinRM(ip_address, 'vagrant', 'vagrant')
        conn.powershell(
            '$result = 1; foreach ($number in 1..2147483647) {$result = $result * $number};'
        )

    def stress_linux_vm(self, ip_address):
        with SSHSession(
            ip_address, username='vagrant', password='vagrant'
        ) as conn:
            conn.execute('timeout 1200 stress --cpu 4')

    def cpustressstate(self, hostname='r3u35.stc.eng'):
        """Start multiple cpu intensive commands to various vms."""

        # with VCenter(vcenter) as vc:
        linux_ips, win_ips = self.vm_os_list(hostname)

        with Pool(len(linux_ips)) as pool:
            pool.map(self.stress_linux_vm, linux_ips)
        with Pool(len(win_ips)) as pool:
            pool.map(self.stress_windows_vm, win_ips)

    @staticmethod
    def delete_all_ss_and_create_fresh_ss(
        vm_ip, vc_host, endpoint_username, endpoint_password
    ):
        """This function will delete all the old snapshot of the provided vm
        and will create fresh one, also it waits until vm is up and running.

        :param vm_ip: IP of vm
        :param vc_host: vcenter host where vm resides
        :param endpoint_username: user name of vm
        :param endpoint_password: password of vm
        :return: bool
        """
        vc = VCenter(vc_host)
        logger.info(f'Getting vm name by vm ip {vm_ip}...')
        vm_name = vc.get_vm_name_by_ip(vm_ip)
        logger.info(f'Deleting all snapshot of vm: {vm_name} ...')
        vc.delete_all_snapshots_by_machine_name(vm_name)
        logger.info(f'Taking fresh snapshot of vm {vm_name} ...')
        vc.take_snapshot(
            vm_ip,
            snap_name='Base OS',
            desc=f'Installed windows update on {date.today().strftime("%B %d, %Y")}',
        )
        logger.info(
            f'Snapshot created successfully, now waiting for valid ip of vm {vm_name} ...'
        )
        wait_for_valid_ip(vm_name, vc, endpoint_username, endpoint_password)
        return True
