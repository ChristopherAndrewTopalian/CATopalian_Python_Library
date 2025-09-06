# getYearMonthDay24.py
# 2025-09-05 21:42:02.290152

from datetime import datetime

def getYearMonthDay24():
    dateTime = datetime.now()
    dateTime.strftime("%Y/%m/%d")

    return dateTime

####

if __name__ == '__main__':
    print(getYearMonthDay24())

    input('Press Enter to Exit')

####

'''
2025-09-05 21:42:02.290152
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

