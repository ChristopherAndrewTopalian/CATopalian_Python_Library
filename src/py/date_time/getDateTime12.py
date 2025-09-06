# getDateTime12.py
# 09-06-25 05:10 AM

import datetime as dt

def getDateTime12():
    currentDateTime = dt.datetime.now()

    # formatted date MM-DD-YY
    date = currentDateTime.strftime("%m-%d-%y")

    # formatted time HH:MM AM/PM
    time = currentDateTime.strftime("%I:%M %p")

    formattedDateTime = date + " " + time

    return formattedDateTime

####

if __name__ == '__main__':
    print(getDateTime12())

    input('Press Enter to Exit')

####

'''
09-06-25 05:10 AM
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

