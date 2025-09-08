# filterByDay.py
# returns only the items from a list that match the given day (ignores year and month)

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

def filterByDay(whichList, whichDay):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # slice out just the day part (characters 8 and 9 of "YYYY-MM-DD")
        dayPart = dateString[8:10]

        # if the day matches, add this item into the result list
        if dayPart == whichDay:
            result.append(whichList[z])

    # return the new list containing only items with the given day
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching for the 09th ("09")
    dayNinePeople = filterByDay(people, '09')

    # print the filtered list so we can see the result
    print(dayNinePeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

