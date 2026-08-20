# get_date_time_12.py    09-06-25 05:10 AM

import datetime as dt

def get_date_time_12():
    currentDateTime = dt.datetime.now()

    # formatted date MM-DD-YY
    date = currentDateTime.strftime("%m-%d-%y")

    # formatted time HH:MM AM/PM
    time = currentDateTime.strftime("%I:%M %p")

    formattedDateTime = date + " " + time

    return formattedDateTime

####

if __name__ == '__main__':
    print(get_date_time_12())
    input('Press Enter to Exit')

'''
09-06-25 05:10 AM
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

