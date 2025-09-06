# filterShowAll.py

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

def filterShowAll(whichList):
    result = []

    for z in range(len(whichList)):
        result.append(whichList[z])

    return result

####

if __name__ == '__main__':
    allPeople = filterShowAll(people)

    print(allPeople)

####

'''
[{'name': 'Jane', 'date': '2024-05-01 10:00:00'}, {'name': 'Jennifer', 'date': '2023-03-12 15:30:00'}, {'name': 'Tabitha', 'date': '2024-05-09 08:45:00'}]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# filterShowAll.py
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

