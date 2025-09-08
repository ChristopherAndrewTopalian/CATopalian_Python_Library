# getMaxByKey.py
# finds the largest value for a given key inside a list of dictionaries

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

def getMaxByKey(listOfDicts, keyName):
    # start by assuming the first item's key value is the maximum
    maxValue = listOfDicts[0][keyName]

    # loop through every dictionary in the list
    for z in range(len(listOfDicts)):
        # get the value for the specified key in the current dictionary
        value = listOfDicts[z][keyName]

        # if this value is larger than the current maximum, update the maximum
        if (value > maxValue):
            maxValue = value

    # return the largest value found for the given key
    return maxValue

####

if __name__ == '__main__':
    # call the function with our people list, looking for the maximum "score"
    maximumScore = getMaxByKey(people, "score")

    # print the largest score so we can see the result
    print(maximumScore)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
98
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

