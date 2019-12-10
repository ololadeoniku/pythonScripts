#print("Hello World")

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

today = date.today()
print(f"Today's date is {today}")
print(f"Date components are {today.day} {today.month} {today.year}")
#print(f"today's weekday # is {today.weekday()}")
days = ["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(f"Today's weekday # is {today.weekday()}, which is a {days[today.weekday()]}")

myTime = datetime.now()
print(myTime)
onlyTime = datetime.time(myTime)
print(onlyTime)
print(myTime.strftime("%A, %d %B %Y"))
print("Locale date and time is" + " " + myTime.strftime("%c"))
print(f"Locale date is" + " " + myTime.strftime("%x"))
print(f"Locale time is" + " " + myTime.strftime("%X"))
print(myTime.strftime("Another way to see current time is: %I:%M:%S %p"))
print(myTime.strftime("or like this: %H:%M"))
print(f"Two and half years from now it will be {today + timedelta(days = (365*2.5))}")
afd = date(today.year, 4, 1)
difference_days = today - afd
if afd < today:
    print(f"April Fool's day passed by {difference_days.days} days ago and it will be {365 - difference_days.days} days till next April fool's day")
c = calendar.TextCalendar(calendar.SUNDAY)
myCalendar = c.formatmonth(2017,1,0,0)
print(myCalendar)
# myCalendarHTML = calendar.HTMLCalendar(calendar.SUNDAY).formatmonth(2017,1)
# print(myCalendarHTML)
daysMonth = c.itermonthdays(2017, 8)
for i in daysMonth:
    print(i)
for i in calendar.day_name:
    print(i)
for j in calendar.month_name:
    print(j)


print("Days for meeting in 2019: First Friday of the month")
for m in range(1,13):
    cal = calendar.monthcalendar(2019, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))
