# filterShowAllNames.py
# returns a list containing all names from the items in the dictionary

people = {
    "jane": {
        "name": "Jane",
        "date": "2024-05-01 10:00:00"
    },
    "jennifer": {
        "name": "Jennifer",
        "date": "2023-05-01 15:30:00"
    },
    "tabitha": {
        "name": "Tabitha",
        "date": "2024-05-09 08:45:00"
    }
}

####

def filterShowAllNames(whichList):
    # start with an empty list to hold our extracted names
    result = []

    # loop through every key in the given dictionary
    for key in whichList:

        # grab the name string from the current item
        nameString = whichList[key]['name']

        # add this name string into the result list
        result.append(nameString)

    # return the new flat list containing only the names
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary to get all names
    allNames = filterShowAllNames(people)

    # print the list of all names so we can see the result
    print(allNames)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
['Jane', 'Jennifer', 'Tabitha']
'''

'''
['Jane',
'Jennifer',
'Tabitha']
'''

'''
Even when our primary database is a complex dictionary of dictionaries, we can easily pull out a single property, like a roster of names, and pack it into a simple, flat array using .append().
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

