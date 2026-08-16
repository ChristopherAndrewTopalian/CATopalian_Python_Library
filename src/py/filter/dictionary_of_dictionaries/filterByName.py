# filterByName.py
# returns only the items from a dictionary that match the given name (case-insensitive)

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

def filterByName(whichList, targetName):
    # start with an empty dictionary
    result = {}

    # loop through every key in the given dictionary
    for key in whichList:

        # grab the name string from the current item
        itemName = whichList[key]['name']

        # compare both itemName and targetName in lowercase (case-insensitive)
        if (itemName.lower() == targetName.lower()):

            # assign the entire profile object to our new dictionary using the same key
            result[key] = whichList[key]

    # return the new dictionary containing only items with the given name
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary, searching for "jane" (lowercase works too)
    namePeople = filterByName(people, "jane")

    # print the filtered dictionary so we can see the result
    print(namePeople)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

