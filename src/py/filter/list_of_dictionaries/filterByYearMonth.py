# filterByYearMonth.py
# returns all items of a list that match a given year and month

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

def filterByYearMonth(whichList, whichMonth):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):
        # check if the date starts with the month string
        if whichList[z]['date'].startswith(whichMonth):
            # append (add) the matching item into the result list
            result.append(whichList[z])

    # return the new list containing only the matching items
    return result

####

if __name__ == '__main__':
    # call the function with our people list and the month '2024-05'
    filteredPeople = filterByYearMonth(people, '2024-05')

    # print the filtered list so we can see the result
    print(filteredPeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}, {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# filterShowAll.py
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

