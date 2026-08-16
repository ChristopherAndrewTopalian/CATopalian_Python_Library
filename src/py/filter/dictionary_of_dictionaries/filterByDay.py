# filterByDay.py
# returns only the items from a dictionary that match the given day (ignores year and month)

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

def filterByDay(whichList, whichDay):
    # start with an empty dictionary
    result = {}

    # loop through every key in the given dictionary
    for key in whichList:
        # grab the date string from the current item
        dateString = whichList[key]['date']

        # slice out just the day part (characters 8 and 9 of "YYYY-MM-DD")
        dayPart = dateString[8:10]

        # if the day matches, add this item into the result dictionary
        if (dayPart == whichDay):
            result[key] = whichList[key]

    # return the new dictionary containing only items with the given day
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary, searching for the 09th ("09")
    dayNinePeople = filterByDay(people, '09')

    # print the filtered dictionary so we can see the result
    print(dayNinePeople)

    input('Press Enter to Exit')

####

'''
{'tabitha': {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}}
'''

'''
{
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

