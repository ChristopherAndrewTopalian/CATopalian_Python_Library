# getMonthNumber.py
# 9

import datetime as dt

def getMonthNumber():
    currentDate = dt.datetime.now()

    # 1 is Jan, 12 is December
    month = currentDate.month

    return month

####

if __name__ == '__main__':
    print(getMonthNumber())

    input('')

####

'''
9
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

