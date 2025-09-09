# getMin.py
# finds the smallest value inside a list of numbers

# create a list of numbers
numbers = [16, 23, 17, 7]

####

def getMin(whichList):
    # find the lowest value in the given list using Python's built-in min() function
    lowestValue = min(whichList)

    # return the lowest value back to the caller
    return lowestValue

####

if __name__ == '__main__':
    # call the function with our numbers list
    minimum = getMin(numbers)

    # print the lowest value so we can see the result
    print(minimum)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
7
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

