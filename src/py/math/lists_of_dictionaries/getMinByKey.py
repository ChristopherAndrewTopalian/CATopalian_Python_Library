# getMinByKey.py
# finds the smallest value for a given key inside a list of dictionaries

# create a sample list of dictionaries
people = [
    {
        "name": "Jane",
        "score": 98
    },

    {
        "name": "Jennifer",
        "score": 90
    },

    {
        "name": "Tabitha",
        "score": 97
    }
]

####

def getMinByKey(listOfDicts, keyName):
    # start by assuming the first item's key value is the minimum
    minValue = listOfDicts[0][keyName]

    # loop through every dictionary in the list
    for z in range(len(listOfDicts)):
        # get the value for the specified key in the current dictionary
        value = listOfDicts[z][keyName]

        # if this value is smaller than the current minimum, update the minimum
        if (value < minValue):
            minValue = value

    # return the smallest value found for the given key
    return minValue

####

if __name__ == '__main__':
    # call the function with our people list, looking for the minimum "score"
    minimumScore = getMinByKey(people, "score")

    # print the smallest score so we can see the result
    print(minimumScore)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
90
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

