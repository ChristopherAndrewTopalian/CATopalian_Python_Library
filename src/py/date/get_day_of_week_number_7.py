# get_day_of_week_number_7.py    6

import datetime as dt

def get_day_of_week_number_7():
    now = dt.datetime.now()

    # monday is 0, sunday is 6
    dayOfWeekNumber = now.weekday()

    # adjust so that monday is 1, sunday is 7
    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted

####

if __name__ == '__main__':
    print(get_day_of_week_number_7())
    input('Press Enter to Exit')

'''
returns: 3, if today is wednesday
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

