# filterByMonthDay.py
# returns only the items from a list that match the given month and day (ignores year and time)

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
    },

    {
        "name": "Alex",
        "date": "2024-05-01 14:20:00"
    }
]

####

from datetime import datetime

def filterByMonthDay(whichList, targetMonth, targetDay):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the month and day match the target, keep it
        if (itemDate.month == targetMonth and itemDate.day == targetDay):
            result.append(whichList[z])

    # return the new list containing only items with the given month and day
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching for May 1 (month=5, day=1)
    monthDayPeople = filterByMonthDay(people, 5, 1)

    # print the filtered list so we can see the result
    print(monthDayPeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}, {'name': 'Jennifer', 'date': '2023-05-01 15:30:00'}, {'name': 'Alex', 'date': '2024-05-01 14:20:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

