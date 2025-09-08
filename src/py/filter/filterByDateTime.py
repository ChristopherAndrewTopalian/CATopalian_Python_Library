# filterByDateTime.py
# returns only the items from a list that exactly match the given date and time

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

from datetime import datetime

def filterByDateTime(whichList, targetDate):
    # start with an empty list
    result = []

    # convert the targetDate string into a datetime object
    target = datetime.strptime(targetDate, "%Y-%m-%d %H:%M:%S")

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the item date is exactly the same as the target, keep it
        if (itemDate == target):
            result.append(whichList[z])

    # return the new list containing only items with the given date
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching for May 1, 2024 at 10:00 AM
    exactDatePeople = filterByDateTime(people, "2024-05-01 10:00:00")

    # print the filtered list so we can see the result
    print(exactDatePeople)

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

