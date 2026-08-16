# filterByMonth.py
# returns only the items from a dictionary that match the given month

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

####

def filterByMonth(whichList, whichMonth):
    # start with an empty dictionary
    result = {}

    # loop through every key in the given dictionary
    for key in whichList:
        # grab the date string from the current item
        dateString = whichList[key]['date']

        # slice out just the month part (characters 5 and 6 of "YYYY-MM-DD")
        monthPart = dateString[5:7]

        # if the month matches, add this item into the result dictionary
        if monthPart == whichMonth:
            result[key] = whichList[key]

    # return the new dictionary containing only items with the given month
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary, searching for May ("05")
    mayPeople = filterByMonth(people, "05")

    # print the filtered dictionary so we can see the result
    print(mayPeople)

    input('Press Enter to Exit')

####

'''
{'jane': {'name': 'Jane', 'date': '2024-05-01 10:00:00'}, 'tabitha': {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}}
'''

'''
{
    'jane':
    {
        'name': 'Jane',
        'date': '2024-05-01 10:00:00'
    },
    'tabitha':
    {
        'name': 'Tabitha',
        'date': '2024-05-09 08:45:00'
    }
}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

