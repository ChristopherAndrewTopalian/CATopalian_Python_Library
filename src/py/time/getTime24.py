# getTime24.py
# 05:53:49

import datetime as dt

def getTime24():
    now = dt.datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    return currentTime

####

if __name__ == '__main__':
    print(getTime24())

    input('Press Enter to Exit')

####

'''
05:53:49
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

