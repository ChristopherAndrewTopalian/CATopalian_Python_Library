# filterByDateTime.py
# returns only the items from a dictionary that exactly match the given date and time

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
    }
}

def filterByDateTime(whichList, targetDate):
    # start with an empty dictionary
    result = {}

    # convert the targetDate string into a datetime object
    target = datetime.strptime(targetDate, "%Y-%m-%d %H:%M:%S")

    # loop through every key in the given dictionary
    for key in whichList:
        # grab the date string from the current item
        dateString = whichList[key]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the item date is exactly the same as the target, keep it
        if (itemDate == target):
            # assign the entire profile object to our new dictionary using the same key
            result[key] = whichList[key]

    # return the new dictionary containing only items with the exact given date and time
    return result

if __name__ == '__main__':
    # call the function with our people dictionary, searching for May 1, 2024 at 10:00 AM
    exactDatePeople = filterByDateTime(people, "2024-05-01 10:00:00")

    # print the filtered dictionary so we can see the result
    print(exactDatePeople)

    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

