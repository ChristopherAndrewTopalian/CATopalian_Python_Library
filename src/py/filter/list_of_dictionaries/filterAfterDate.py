# filterAfterDate.py
# returns only the items from a list that have a date greater than the given date

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

def filterAfterDate(whichList, cutoffDate):
    # start with an empty list
    result = []

    # convert the cutoffDate string into a datetime object
    cutoff = datetime.strptime(cutoffDate, "%Y-%m-%d %H:%M:%S")

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the item date is greater than the cutoff date, keep it
        if (itemDate > cutoff):
            result.append(whichList[z])

    # return the new list containing only items after the cutoff
    return result

####

if __name__ == '__main__':
    # call the function with our people list, using May 2, 2024 as the cutoff
    afterDatePeople = filterAfterDate(people, "2024-05-02 00:00:00")

    # print the filtered list so we can see the result
    print(afterDatePeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

