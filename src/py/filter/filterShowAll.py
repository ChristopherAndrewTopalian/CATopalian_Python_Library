# filterShowAll.py
# returns all the items of a list

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

def filterShowAll(whichList):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):
        # append (add) each item into the result list
        result.append(whichList[z])

    # return the new list containing all items
    return result

####

if __name__ == '__main__':
    # call the function with our people list
    allPeople = filterShowAll(people)

    # print the entire list so we can see the result
    print(allPeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'},
 {'name': 'Jennifer', 'date': '2023-03-12 15:30:00'},
 {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

