import time, datetime

now = int(time.time())
timeArray = time.localtime(now)
otherTimeStyle_Ymd = time.strftime("%Y%m%d", timeArray)
otherTimeStyle_Hms = time.strftime("%H:%M:%S", timeArray)

print(now, type(now))
print(timeArray)
print(otherTimeStyle_Ymd)
print(isinstance(otherTimeStyle_Hms, str))
print(otherTimeStyle_Hms)
