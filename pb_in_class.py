
phonebook = {
            'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'Lambda': {'name': 'Lambda',
                         'number': 8454185633,
                         'phrase': 'I am a robot.'
                         }
            }

def add_contact(name, phone, phrase):
    pass


def search(query):
    entries_list = []
    if query in phonebook:
        entries_list.append(phonebook[query]['name'], phonebook[query]['number'], phonebook[query]['phrase'])
    else:
        for entry in phonebook:
            for item in entry:
                print('query: {}'.format(query))
                if query in item:
                    return entry


def update(name, phone, phrase):
    pass


def remove(query): #delete((phonebook[key]))
    pass


def display(entry):
    print('Name: {}'.format(entry['name']))
    print('Phone: {}'.format(entry['phone']))
    print('Phrase: {}'.format(entry['phrase']))

def menu():
    while True:
        q = input("Would you like to (a)dd (s)earch (u)pdate (r)emove or (q)uery").lower()
        if q == 's':
            search_term = input("Enter name number or phrase you want to search (partial or whole)")
            search()
        elif q == 'a':

        elif q == 'u':

        elif q == 'r':

        elif q == 'q':

        else:
            print("I didn't understand that, try again.")

menu()
