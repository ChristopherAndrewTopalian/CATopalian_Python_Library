# filterByMonth.py
# returns only the items from a list that match the given month

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

def filterByMonth(whichList, whichMonth):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):
        # grab the date string from the current item
        dateString = whichList[z]['date']

        # slice out just the month part (characters 5 and 6 of "YYYY-MM-DD")
        monthPart = dateString[5:7]

        # if the month matches, add this item into the result list
        if monthPart == whichMonth:
            result.append(whichList[z])

    # return the new list containing only items with the given month
    return result

####

if __name__ == '__main__':
    # call the function with our people list, searching for May ("05")
    mayPeople = filterByMonth(people, "05")

    # print the filtered list so we can see the result
    print(mayPeople)

    input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}, {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

