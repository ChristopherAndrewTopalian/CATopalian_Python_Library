# filterByYear.py
# returns only the items where the date starts with the given year

people = [
    {
        "name": "Jane",
        "date": "2024-05-01 10:00:00"
    },

    {
        "name": "Jennifer",
        "date": "2023-03-12 15:30:00"
    },

    {
        "name": "Tabitha",
        "date": "2024-05-09 08:45:00"
    }
]

####

def filterByYear(whichArray, whichYear):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichArray)):
        # check if the 'date' field starts with the given year
        if whichArray[z]["date"].startswith(whichYear):
            # if it matches, add it to the result list
            result.append(whichArray[z])

    # return the new filtered list
    return result

####

if __name__ == '__main__':
    # call the function with our people list and target year
    filteredPeople = filterByYear(people, "2024")

    # print the filtered list so we can see the result
    print(filteredPeople)

    input("Press Enter to Exit")

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}, {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

