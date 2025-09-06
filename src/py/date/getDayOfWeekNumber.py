# getDayOfWeekNumber.py
# 7

import datetime as dt

def getDayOfWeekNumber():
    now = dt.datetime.now()

    # python's weekday(): monday=0 ... sunday=6
    dayOfWeekNumber = now.weekday()

    # shift so sunday=0 ... saturday=6
    dayOfWeekNumber = (dayOfWeekNumber + 1) % 7

    # shift so sunday=1 ... saturday=7
    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted

####

if __name__ == '__main__':
    print(getDayOfWeekNumber())

    input('Press Enter to Exit')

####

'''
example:
returns 4 if wednesday
returns 7 if saturday
returns 1 if sunday
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting


