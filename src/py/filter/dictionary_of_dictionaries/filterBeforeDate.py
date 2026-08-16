# filterBeforeDate.py
# returns only the items from a dictionary that have a date less than the given date

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

def filterBeforeDate(whichList, cutoffDate):
    # start with an empty dictionary
    result = {}

    # convert the cutoffDate string into a datetime object
    cutoff = datetime.strptime(cutoffDate, "%Y-%m-%d %H:%M:%S")

    # loop through every key in the given dictionary
    for key in whichList:
        # grab the date string from the current item
        dateString = whichList[key]['date']

        # convert the date string into a datetime object
        itemDate = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")

        # if the item date is less than the cutoff date, keep it
        if (itemDate < cutoff):
            # assign the entire profile object to our new dictionary using the same key
            result[key] = whichList[key]

    # return the new dictionary containing only items before the cutoff
    return result

if __name__ == '__main__':
    # call the function with our people dictionary, using May 2, 2024 as the cutoff
    beforeDatePeople = filterBeforeDate(people, "2024-05-02 00:00:00")

    # print the filtered dictionary so we can see the result
    print(beforeDatePeople)

    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}, 'jennifer': {'name': 'Jennifer', 'date': '2023-03-12 15:30:00'}}
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
        'date': '2023-03-12 15:30:00'
    }
}
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

