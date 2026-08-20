# filterShowAllNames.py
# returns a list containing all names from the items in the list

people = [
    {
        "name": "Jane",
        "date": "2024-05-01 10:00:00"
    },

    {
        "name": "Jennifer",
        "date": "2023-05-01 15:30:00"
    },

    {
        "name": "Tabitha",
        "date": "2024-05-09 08:45:00"
    }
]

####

def filterShowAllNames(whichList):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):

        # grab the name string from the current item
        nameString = whichList[z]['name']

        # add this name string into the result list
        result.append(nameString)

    # return the new list containing only the names
    return result

####

if __name__ == '__main__':
    # call the function with our people list to get all names
    allNames = filterShowAllNames(people)

    # print the list of all names so we can see the result
    print(allNames)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
['Jane', 'Jennifer', 'Tabitha']
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

