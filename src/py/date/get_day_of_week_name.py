# get_day_of_week_name.py    Monday

import datetime as dt

def get_day_of_week_name():
    currentDate = dt.datetime.now()

    # 0 is Monday, 6 is Sunday
    dayOfWeek = currentDate.weekday()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # get name of day using day of week index
    dayName = days[dayOfWeek]

    return dayName

####

if __name__ == '__main__':
    print(get_day_of_week_name())
    input('Press Enter to Exit')

'''
Monday
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

