# filterBetweenDates.py
# returns only the items from a list that have a date between two given cutoff dates

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

def filterBetweenDates(whichList, startDate, endDate):
    # start with an empty list
    result = []

    # convert the startDate and endDate strings into datetime objects
    start = datetime.strptime(startDate, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(endDate, "%Y-%m-%d %H:%M:%S")

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the item date is between the two cutoffs, keep it
        if (itemDate >= start and itemDate <= end):
            result.append(whichList[z])

    # return the new list containing only items in the given range
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching between May 1 and May 8, 2024
    betweenDatePeople = filterBetweenDates(
        people,
        "2024-05-01 00:00:00",
        "2024-05-08 23:59:59"
    )

    # print the filtered list so we can see the result
    print(betweenDatePeople)

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

