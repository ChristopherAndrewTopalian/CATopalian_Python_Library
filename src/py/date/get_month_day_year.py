# get_month_day_year.py

import datetime as dt

def get_month_day_year():
    today = dt.date.today()

    # %m = Month (01-12)
    # %d = Day (01-31)
    # %Y = Year (4 digits)
    formatted_date = today.strftime("%m-%d-%Y")

    return formatted_date

####

if __name__ == '__main__':
    print(get_month_day_year())
    input('Press Enter to Exit\n')

'''
08-20-2026
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

