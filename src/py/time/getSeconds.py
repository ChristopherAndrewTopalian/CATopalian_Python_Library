# getSeconds.py
# returns current second of the minute (00-59)

import datetime as dt

def getSeconds():
    now = dt.datetime.now()
    # extract seconds as a zero padded string
    currentSeconds = now.strftime("%S")

    return currentSeconds

####

if __name__ == '__main__':
    print(getSeconds())

    input('Press Enter to Exit')

####

'''
10
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

