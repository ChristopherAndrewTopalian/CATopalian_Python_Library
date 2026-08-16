# filterByDate.py
# returns only the items from a dictionary that match the given calendar date (ignores the time)

from datetime import datetime

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
    },
    "ariana": {
        "name": "Ariana",
        "date": "2024-05-01 14:20:00"
    }
}

def filterByDate(whichList, targetDate):
    # start with an empty dictionary
    result = {}

    # convert the targetDate string into a datetime object (date only)
    target = datetime.strptime(targetDate, "%Y-%m-%d").date()

    # loop through every key in the given dictionary
    for key in whichList:
        # grab the date string from the current item
        dateString = whichList[key]['date']

        # convert the date string into a datetime object, then just take the date part
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S").date()

        # if the item date matches the target date, keep it
        if (itemDate == target):
            # assign the entire profile object to our new dictionary using the same key
            result[key] = whichList[key]

    # return the new dictionary containing only items with the given date
    return result

if __name__ == '__main__':
    # call the function with our people dictionary, searching for May 1, 2024 (ignores the time)
    datePeople = filterByDate(people, "2024-05-01")

    # print the filtered dictionary so we can see the result
    print(datePeople)

    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}, 'ariana': {'name': 'Ariana', 'date': '2024-05-01 14:20:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    },
    'ariana':
    {
        'name': 'Ariana',
        'date': '2024-05-01 14:20:00'
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

