# getMinutes.py
# returns current minute of the hour (00-59)

import datetime as dt

def getMinutes():
    now = dt.datetime.now()
    # extract the minute as a zero padded string
    currentMinute = now.strftime("%M")

    return currentMinute

####

if __name__ == '__main__':
    print(getMinutes())

    input('Press Enter to Exit')

####

'''
27
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

