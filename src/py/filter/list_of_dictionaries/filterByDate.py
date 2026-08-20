# filterByDate.py
# returns only the items from a list that match the given calendar date (ignores the time)

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
    },

    {
        "name": "Ariana",
        "date": "2024-05-01 14:20:00"
    }
]

####

from datetime import datetime

def filterByDate(whichList, targetDate):
    # start with an empty list
    result = []

    # convert the targetDate string into a datetime object (date only)
    target = datetime.strptime(targetDate, "%Y-%m-%d").date()

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # convert the date string into a datetime object, then just take the date part
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S").date()

        # if the item date matches the target date, keep it
        if (itemDate == target):
            result.append(whichList[z])

    # return the new list containing only items with the given date
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching for May 1, 2024 (ignores the time)
    datePeople = filterByDate(people, "2024-05-01")

    # print the filtered list so we can see the result
    print(datePeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}, {'name': 'Ariana', 'date': '2024-05-01 14:20:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

