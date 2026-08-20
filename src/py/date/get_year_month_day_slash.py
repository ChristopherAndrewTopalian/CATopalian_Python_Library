# get_year_month_day_slash.py    2025/9/5

from datetime import datetime

def get_year_month_day_slash():
    dateTime = datetime.now()
    year = dateTime.year
    month = dateTime.month
    day = dateTime.day

    yearMonthDay = f"{year}/{month}/{day}"

    return yearMonthDay

####

if __name__ == '__main__':
    print(get_year_month_day_slash())
    input('Press Enter to Exit')

'''
2025/9/5
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

