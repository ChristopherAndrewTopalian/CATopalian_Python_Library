# filterShowAll.py
# returns all the items of a dictionary

people = {
    "jane": {
        "name": "Jane",
        "date": "2024-05-01 10:00:00"
    },
    "jennifer": {
        "name": "Jennifer",
        "date": "2023-03-12 15:30:00"
    },
    "tabitha": {
        "name": "Tabitha",
        "date": "2024-05-09 08:45:00"
    }
}

####

def filterShowAll(whichList):
    # start with an empty dictionary
    result = {}

    # loop through every key in the given dictionary
    for key in whichList:
        # assign the entire profile object to our new dictionary using the same key
        result[key] = whichList[key]

    # return the new dictionary containing all items
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary
    allPeople = filterShowAll(people)

    # print the entire dictionary so we can see the result
    print(allPeople)

    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}, 'jennifer': {'name': 'Jennifer', 'date': '2023-03-12 15:30:00'}, 'tabitha': {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    },
    'jennifer':
    {
        'name': 'Jennifer',
        'date': '2023-03-12 15:30:00'
    },
    'tabitha':
    {
        'name': 'Tabitha',
        'date': '2024-05-09 08:45:00'
    }
}
'''

'''
While making an exact copy of a dictionary is actually built directly into Python (using people.copy()), building this function manually is an excellent foundational exercise for the cadets. It shows them the basic mechanics of how to loop through and reconstruct a dictionary key by key before they start adding complex conditions.
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

