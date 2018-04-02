phonebook = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'Lambda': {'name': 'Lambda',
                         'number': 8454185633,
                         'phrase': 'I am a robot.'}}

print("***Welcome to your phonebook***")


def phonebook_overview():
    as_of_now = input("Do you want to look at your current phonebook? y/n: ")
    if as_of_now == "y":
        print(phonebook)

(phonebook_overview())

def create_new_contact():
    create_new = input("Do you want to create a new contact? y/n: ")
    if create_new == "y":
        na = input("What is the new contact name?: ")
        num = input("What is the phone number?: ")
        phr = input("Give me a brief info phrase about contact: ")
    return na, num, phr
    # new_contact = name, number, phrase

na, num, phr = create_new_contact()

phonebook[na] = {'name': na, 'number': num, 'phrase': phr}

print(phonebook)

# def add_to_dictionary():
#     return add_to_dictionary
# print(phonebook)
# #(create_new_contact())
# # print(phonebook)
