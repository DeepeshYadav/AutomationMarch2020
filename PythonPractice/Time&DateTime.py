import time
import datetime

# print as ctime
print(time.asctime())

# print local time
print(time.localtime())

#print time
print(time.time())

#print(dir(time))

#print(dir(datetime))

print(datetime.time())

time_local = time.localtime()
print(time_local[0])

##########################################

import calendar

print(calendar.isleap(2013))
