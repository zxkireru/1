from datetime import datetime
from datetime import timedelta

now = datetime.now()
birthday = datetime(2003,5,27)
averageman = 60.5
averagewoman = 67.5
datelive = birthday + timedelta(days=averageman*365)
timeleft = datelive - now

print(timeleft.days)