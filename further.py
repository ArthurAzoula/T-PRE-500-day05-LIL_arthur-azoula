# task 01

names = ["Arthur", "Olivier", "Pierre", "Yann"]


def inList(tab, name):
    return name in tab

def displayList(tab, name):
    if inList(tab, name):
        return 'Welcome in'
    return 'Get lost'

print(displayList(names, 'Arthur'))

# task 02

def deleteDoubles(tab):
    new_tab =  []
    
    for element in tab:
        if element not in new_tab:
            new_tab.append(element)

    return new_tab

print(deleteDoubles([1,23,32,1,4,5,4,9,19]))

# task 03 

meetings = []

def createNewMeeting(day, hours, *participants) -> dict:
    meeting = {
        "day": day,
        "hours": hours,
        "participants": list(participants)
    }
    meetings.append(meeting)

def displayMeeting(meeting: dict):
    print(f"--------------------------------------------------------------------")
    print(f"DAY: {meeting['day']}")
    print(f"TIME: {meeting['hours']}")
    print(f"PARTICIPANTS: {', '.join(meeting['participants'])}")
    print(f"--------------------------------------------------------------------")

createNewMeeting('Monday', '3:30 PM', 'Joe', 'Samantha', 'John')
createNewMeeting('Tuesday', '2:00 PM', 'Alice', 'Bob', 'Joe')
createNewMeeting('Wednesday', '4:45 PM', 'Samantha', 'John', 'Alice')

def displayMeetingByPerson(person_name):
    print(f"Meetings involving {person_name}:")
    for meeting in meetings:
        if person_name in meeting['participants']:
            displayMeeting(meeting)

displayMeetingByPerson('Samantha')