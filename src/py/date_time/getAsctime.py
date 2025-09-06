# getAsctime.py
# Sat Sep  6 05:25:27 2025

import time

def getAsctime():
    # get current time formatted as a string in old-style C format
    asctimeString = time.asctime()
    return asctimeString

####

if __name__ == '__main__':
    print(getAsctime())

####

'''
example output:
Sat Sep  6 12:34:56 2025
(note the double space before the "6")
'''

####

'''
why does asctime() have double spaces for single-digit days?

- time.asctime() always returns a fixed-width string in the format:
    Www Mmm dd hh:mm:ss yyyy
    where:
        Www = day of week (3 letters)
        Mmm = month (3 letters)
        dd  = day of month (always 2 characters wide, padded with a space if < 10)
        hh:mm:ss = time
        yyyy = year

- for example:
    "Sat Sep  6 12:34:56 2025"   # day is 6 → padded with a space
    "Mon Sep 16 12:34:56 2025"   # day is 16 → two digits, no extra space

- this design comes directly from the C standard library's asctime() function.
  python inherited it for compatibility. the formatting is fixed-width, so that
  all fields always align in columns when displayed in old console programs.

- if you want modern, flexible formatting (no quirks, no double spaces), use time.strftime().
  for example:
      time.strftime("%A, %B %d, %Y, %H:%M:%S")
  → "Saturday, September 06, 2025, 12:34:56"

so in short:
- asctime() = old-school, fixed-width, quirky but predictable
- strftime() = modern, customizable, recommended for real-world projects
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

