# getHour.py
# returns current hour in 24 hour format

import datetime as dt

def getHour():
    now = dt.datetime.now()
    # 0-23
    currentHour = now.hour
    return currentHour

####

if __name__ == '__main__':
    print(getHour())

    input('Press Enter to Exit')

####

'''
5
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

