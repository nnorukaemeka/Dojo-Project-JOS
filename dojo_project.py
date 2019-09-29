""" 
************ Code Plateau 1.0 Bootcamp **************
The Dojo Project is about a system that automatically allocates an office to a new Code Plateau staff, and an office with (optional living space) to a new Code Plateau Participant. 
Let's introduce five(5) Functions used in the Project:
1. get_started(staff,participant) - this first function is used to get ALL the inputs from a user and depending on certain conditions met, it takes the user to either the second function 'alloc_office(person)', or the third function 'alloc_living_space(person)' or even quits the program and displays the Room Allocation Analysis in Dojo.
2. alloc_office(person) - this second function takes care of the allocation of offices to Staff and Participants(who don't opt in for a living space).
3. alloc_living_space(person) - this is the third function that allocates both an office and a living space to a Participant ONLY. (This function is allergic to Staff... lol)
4. new_office(kold) - this function creates new office with six (6) spaces inside (e.g 'office1_table1,...,office1_table6'). Remember the constraint given in the question that states: 'An office can accommodate a maximum of 6 people' i.e 6 tables!
5. new_living(hold) - this last function is similar to 'new_office(kold)'. While 'new_office(kold)' creates new office with six spaces inside, new_living(hold) creates new living space with four (4) rooms inside (e.g 'room1_bed1,...,room1_bed4'). Also, the constraint states: 'A living space can accommodate a maximum of 4 people' i.e 4 beds!

Wait! see as I'm turning this page to a 'README'.  Enough biko...! 
But don't forget to used 'PYTHON3 version' to run this code.
Explore and have great FUN!!!!
"""


def get_started(staff,participant):
    try:
        detail = int(input ("Enter 1 to provide your details, 0 to exit :::  \n"))
        person = {}
        if detail == 1:
            name = input ("Enter your name :::  \n")
            person["name"] = name
            category = int(input ("Enter 1 for 'Staff', 2 for 'Participant'  ::: \n"))
            if category == 1:
                person["category"] = "staff"
                staff_id = int(input ("Enter Staff ID number (e.g 0023)  ::: \n"))
                if len(staff) !=0:
                    for i in staff:
                        if i['id'] == staff_id:
                            print ("Staff already exist!\n")
                            get_started(staff,participant)
                person["id"] = staff_id
                alloc_office(person)
                staff.append(person)
            elif category == 2:
                person["category"] = "participant"
                participant_id = int(input ("Enter Participant ID number (e.g 0023)  ::: \n"))
                if  len(participant) !=0:
                    for i in participant:
                        if i['id'] == participant_id:
                            print ("Participant already exist!\n")
                            get_started(staff,participant)
                person["id"] = participant_id
                alloc_living_space(person)
                participant.append(person)
            else:
                print("You entered an invalid number")
                get_started(staff,participant)
            persons.append(person)
            get_started(staff,participant)
        elif detail == 0:
            #Print break-down of used and unused spaces:
            print(":::: ALLOCATION ANALYSIS IN DOJO  ::::"'\n')
            print(f"Total Number of Registered Persons: {len(persons)} (Staff: {len(staff)}, Participants: {len(participant)})"'\n')
            print("Registered Staff: ", staff,'\n')
            print("Registered Participants: ", participant,'\n')
            print("Details of Occupied Spaces in Dojo: ", occupied_office,'\n')
            print("Unoccupied Living Space: ", living,'\n') 
            print("Unoccupied Offices: ", office,'\n')
            quit()
        else:
            print("You entered an invalid number")
            get_started(staff,participant)
    except ValueError:
        print("Sorry, invalid input!")
        get_started(staff,participant)

def alloc_office(person):
    shuffle(office)
    if len(office) >=1:
        allocated_office = {}
        allocated_office["name"] = person['name']
        allocated_office["category"] = person['category']
        allocated_office["id"] = person['id']
        allocated_office["office"] = office[0]
        occupied_office.append(allocated_office)
        office.pop(0)
        print("Accomodation_details: ", allocated_office,'\n')
    else:
        print("A new office is initialized")
        new_office(kold)
        alloc_office(person)

def alloc_living_space(person):
    shuffle(living)
    if len(office) !=0:
        if len(living) >=1:
            optional = input ("Hello {}, do you need a living space? Y/N :::  " .format(person['name'])).lower()
            if optional == 'y':
                allocated_office = {}
                allocated_office["name"] = person['name']
                allocated_office["category"] = person['category']
                allocated_office["id"] = person['id']
                allocated_office["office"] = office[0]
                allocated_office["living_space"] = living[0]
                occupied_office.append(allocated_office)
                office.pop(0)
                living.pop(0)
                print("Accomodation_details: ", allocated_office, '\n')
            else:
                alloc_office(person)
        else:
            print("A new living space is initialized")
            new_living(hold)
            alloc_living_space(person)
    else:
        print("A new office is initialized")
        new_office(kold)
        alloc_living_space(person)

def new_office(kold):
    k = kold[0] 
    for i in range(1,7):
        office.append('office{}_table{}'.format(k,i))
    k +=1
    kold.append(k)
    kold.pop(0)

def new_living(hold):
    h = hold[0]
    for i in range(1,5):
        living.append('room{}_bed{}'.format(h,i))
    h +=1
    hold.append(h)
    hold.pop(0)


#************ MAIN PROGRAM ************************

# Import random module and Declare variables::
from random import shuffle

kold = [1]
hold = [1]
office = []
living = []
staff = []
participant = []
persons = []
occupied_office = []
occupied_living = []

#call the input function:
get_started(staff,participant)
