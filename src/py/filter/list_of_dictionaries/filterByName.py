# filterByName.py
# returns only the items from a list that match the given name (case-insensitive)

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

def filterByName(whichList, targetName):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):

        # grab the name string from the current item
        itemName = whichList[z]['name']

        # compare both itemName and targetName in lowercase (case-insensitive)
        if (itemName.lower() == targetName.lower()):

            # add the matching item into the result list
            result.append(whichList[z])

    # return the new list containing only items with the given name
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching for "jane" (lowercase works too)
    namePeople = filterByName(people, "jane")

    # print the filtered list so we can see the result
    print(namePeople)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

