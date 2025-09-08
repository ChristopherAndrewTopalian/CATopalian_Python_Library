# filterShowAllDates.py
# returns a list containing all dates from the items in the list

people = [
    {
        "name": "Jane",
        "date": "2024-05-01 10:00:00"
    },

    {
        "name": "Jennifer",
        "date": "2023-05-01 15:30:00"
    },

    {
        "name": "Tabitha",
        "date": "2024-05-09 08:45:00"
    }
]

####

def filterShowAllDates(whichList):
    # start with an empty list
    result = []

    # loop through every index in the given list
    for z in range(len(whichList)):

        # grab the date string from the current item
        dateString = whichList[z]['date']

        # add this date string into the result list
        result.append(dateString)

    # return the new list containing only the dates
    return result

####

if __name__ == '__main__':
    # call the function with our people list to get all dates
    allDates = filterShowAllDates(people)

    # print the list of all dates so we can see the result
    print(allDates)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
['2024-05-01 10:00:00', '2023-05-01 15:30:00', '2024-05-09 08:45:00']
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

