# filterByMonthDay.py
# returns only the items from a dictionary that match the given month and day (ignores year and time)

from datetime import datetime

people = {
    "jane": {
        "name": "Jane",
        "date": "2024-05-01 10:00:00"
    },
    "jennifer": {
        "name": "Jennifer",
        "date": "2023-05-01 15:30:00"
    },
    "tabitha": {
        "name": "Tabitha",
        "date": "2024-05-09 08:45:00"
    },
    "alex": {
        "name": "Alex",
        "date": "2024-05-01 14:20:00"
    }
}

####

def filterByMonthDay(whichList, targetMonth, targetDay):
    # start with an empty dictionary
    result = {}

    # loop through every key in the given dictionary
    for key in whichList:
        # grab the date string from the current item
        dateString = whichList[key]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the month and day match the target, keep it
        if (itemDate.month == targetMonth and itemDate.day == targetDay):
            # assign the entire profile object to our new dictionary using the same key
            result[key] = whichList[key]

    # return the new dictionary containing only items with the given month and day
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary, searching for May 1 (month=5, day=1)
    monthDayPeople = filterByMonthDay(people, 5, 1)

    # print the filtered dictionary so we can see the result
    print(monthDayPeople)

    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}, 'jennifer': {'name': 'Jennifer', 'date': '2023-05-01 15:30:00'}, 'alex': {'name': 'Alex', 'date': '2024-05-01 14:20:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    },
    'jennifer':
    {
        'name': 'Jennifer',
        'date': '2023-05-01 15:30:00'
    },
    'alex':
    {
        'name': 'Alex',
        'date': '2024-05-01 14:20:00'
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

