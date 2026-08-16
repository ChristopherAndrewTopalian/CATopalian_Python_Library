# filterShowAllDates.py
# returns a list containing all dates from the items in the dictionary

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
    }
}

####

def filterShowAllDates(whichList):
    # start with an empty list to hold our extracted dates
    result = []

    # loop through every key in the given dictionary
    for key in whichList:

        # grab the date string from the current item
        dateString = whichList[key]['date']

        # add this date string into the result list
        result.append(dateString)

    # return the new flat list containing only the dates
    return result

####

if __name__ == '__main__':
    # call the function with our people dictionary to get all dates
    allDates = filterShowAllDates(people)

    # print the list of all dates so we can see the result
    print(allDates)

    # keep the program open until Enter is pressed
    input('Press Enter to Exit')

####

'''
['2024-05-01 10:00:00', '2023-05-01 15:30:00', '2024-05-09 08:45:00']
'''

'''
['2024-05-01 10:00:00',
'2023-05-01 15:30:00',
'2024-05-09 08:45:00']
'''

'''
Even though we changed our main people database into a dictionary of dictionaries, we still use a standard list ([]) and the .append() method for our result. This teaches them the concept of data extraction, pulling a single specific property out of a complex dictionary and neatly packing it into a simple, flat list.
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

