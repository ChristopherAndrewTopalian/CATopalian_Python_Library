# filterByYear.py
# returns only the items where the date starts with the given year

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

def filterByYear(whichList, whichYear):
    # start with an empty dictionary
    result = {}

    # loop through every key in the given dictionary
    for key in whichList:
        # check if the 'date' field starts with the given year
        if whichList[key]["date"].startswith(whichYear):
            # if it matches, add it to the result dictionary
            result[key] = whichList[key]

    # return the new filtered dictionary
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary and target year
    filteredPeople = filterByYear(people, "2024")

    # print the filtered dictionary so we can see the result
    print(filteredPeople)

    input("Press Enter to Exit")

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}, 'tabitha': {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    },
    'tabitha':
    {
        'name': 'Tabitha',
        'date': '2024-05-09 08:45:00'
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

