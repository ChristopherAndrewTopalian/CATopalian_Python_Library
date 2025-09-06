# getHour12.py
# returns current hour in 12 hour format with AM/PM

import datetime as dt

def getHour12():
    now = dt.datetime.now()
    # format hour in 12 hour clock with AM/PM
    currentHour = now.strftime("%I %p")

    return currentHour

####

if __name__ == '__main__':
    print(getHour12())

    input('Press Enter to Exit')

####

'''
07 AM
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting


