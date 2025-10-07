
import datetime 

def allSunday(year):
    first_day = datetime.date(year,1,1)
    dw = first_day.weekday()
    days = datetime.timedelta(6-dw)

    sun = first_day + days

    while sun.year == year:
        print(sun)
        sun += datetime.timedelta(7)


allSunday(2025)