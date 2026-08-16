# get_max.py
# finds the largest value inside a list of numbers

# create a list of numbers
numbers = [16, 23, 17, 7]

####

def get_max(whichList):
    # find the highest value in the given list using Python's built-in max() function
    highestValue = max(whichList)

    # return the highest value back to the caller
    return highestValue

####

if __name__ == '__main__':
    # call the function with our numbers list
    maximum = get_max(numbers)

    # print the highest value so we can see the result
    print(maximum)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
23
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

