# is_target_date.py

import datetime as dt

def is_target_date(target_string):
    # Get today's date object and instantly convert it to a string
    today_str = str(dt.date.today())
    
    # Now we can safely compare text to text
    if today_str == target_string:
        return True
    else:
        return False

####

if __name__ == '__main__':
    print("System: Checking date authorization...")

    # We pass the date we are looking for into the function
    if is_target_date("2026-08-20"):
        print("Authorization granted. Target date verified.")
    else:
        print("Authorization denied. Date does not match.")

    input('\nPress Enter to Exit')

####

'''
System: Checking date authorization...
Authorization granted. Target date verified.

Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

