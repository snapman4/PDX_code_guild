print("Welcome to your phonebook")

phonebook = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'Lambda': {'name': 'Lambda',
                         'number': 8454185633,
                         'phrase': 'I am a robot.'}}


def create_new_contact():
    create_new = input("Do you want to create a new contact? y/n: ")
    if create_new == "y":
        na = input("What is the new contact name?: ")
        num = input("What is the phone number?: ")
        phr = input("Give me a brief info phrase about contact: ")
    return na, num, phr
    new_contact = name, number, phrase

#na, num, phr = create_new_contact()

#phonebook[na] = {'name': na, 'number': num, 'phrase': phr}

# ##needs work below
# def retrieve_contact():
#     selected = input("What name do you want to get info from your phonebook?: ")
#     return selected
# selected = retrieve_contact()
# print(phonebook.get("selected"))
# #print(retrieve_contact())

#need to figure out to edit parent dictionary br
def update():
    change = input("What do you want to change in your phonebook?: ")
    if change == "name":
        change_to = input("What do you want to change the name to?: ")
        phonebook['name'] = change_to
    elif change == "num":
        change_to = input("What do you want to change the number to?: ")
        phonebook['number'] = change_to
    elif change == "phrase":
        change_to = input("What do you want to change the phrase to?: ")
        phonebook['phrase'] = change_to
    return change, change_to

(update())

def CRUD():
    choice = input("""
            Please choose an option by selecting the first character
            *C*reate New Contact
            *R*etrieve Contact
            *U*pdate Existing Contact
            *D*elete Contact\n:""")
# (CRUD())
#print(phonebook.get('Kieran'))
print(phonebook)
