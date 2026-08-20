# get_month_number.py    9

import datetime as dt

def get_month_number():
    currentDate = dt.datetime.now()

    # 1 is Jan, 12 is December
    month = currentDate.month

    return month

####

if __name__ == '__main__':
    print(get_month_number())
    input('Press Enter to Exit')

'''
9
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

