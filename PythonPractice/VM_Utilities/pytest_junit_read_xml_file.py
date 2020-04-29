from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
from urllib.request import urlopen
import xlwt
from xlwt import Workbook
import datetime

wb = Workbook()

def write_excel_sheet(filename, sheet_name, data):
    sheet = wb.add_sheet(sheet_name)

    #font style
    style_string = "font: bold on; borders: bottom dashed"
    style = xlwt.easyxf(style_string)

    # color style
    stylered = xlwt.easyxf('pattern: pattern solid, fore_colour red;'
                        'font: colour white, bold True;')

    stylegreen = xlwt.easyxf('pattern: pattern solid, fore_colour green;'
                           'font: colour white, bold True;')

    sheet.write(0, 0, 'Test Case', style=style)
    sheet.write(0, 1, 'Status', style=style)
    sheet.write(0, 2, 'RC', style=style)

    row = 1
    for item in data:
        print(item)
        sheet.write(row, 0, item[0]['title'])
        if  item[0]['status'] == 'FAIL':
            sheet.write(row, 1, item[0]['status'], style=stylered)
        elif item[0]['status'] == 'PASS':
            sheet.write(row, 1, item[0]['status'], style=stylegreen)
        row += 1

    wb.save(filename)


def read_xml_data(url_input):

    result_list = []
    for url in url_input:
        var_url = urlopen(url)
        xmldata = parse(var_url)
        root = xmldata.getroot()
        print(root)

        for item in root:
            result_dict = {}
            data_list = []
            #print(item.attrib['name'])
            status = 'PASS'
            for elem in item:
                if elem.tag == 'failure':
                    status = 'FAIL'

            print(f"Title:{item.attrib['name']}, Status : {status}")
            result_dict['title'] = item.attrib['name']
            result_dict['status'] = status
            data_list.append(result_dict)
            if status == 'FAIL':
                result_list.insert(0, data_list)
            else:
                result_list.append(data_list)

    return  result_list

url1 = "http://jar-smoke-03.stc.eng/JAR-P1AAT1938-RS/test/marvin/logs/20200403_070817_JAR-P1AAT1938-RS-103_release_3.1_187/pytestjunit.xml"
url2 = "http://jar-smoke-01.stc.eng/JAR-P1AAT1938-RPP/test/marvin/logs/20200403_070812_JAR-P1AAT1938-RPP-103_release_3.1_187/pytestjunit.xml"
url3 = "http://jar-smoke-03.stc.eng/JAR-WAA-RP/test/marvin/logs/20200403_020631_JAR-WAA-RP-42_develop_4451/pytestjunit.xml"

todays_date = str(datetime.datetime.today()).split()[0]
p1_result = read_xml_data([url1])
write_excel_sheet(f'Automation_status_{todays_date}.xls', 'P1 Test Cases', p1_result)
p2_result = read_xml_data([url2])
write_excel_sheet(f'Automation_status_{todays_date}.xls', 'P2 Test Cases', p2_result)
agent_result = read_xml_data([url3])
write_excel_sheet(f'Automation_status_{todays_date}.xls', 'Windows Agent TestCases', agent_result)
