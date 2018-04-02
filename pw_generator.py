import random
import string


number_of_characters = int(input("How many characters do you want in your password?: "))

def available_characters():
    options = string.printable
    return options

#print(available_characters())

characters = available_characters()


def password_builder():
    password = " "
    for i in range (0, number_of_characters):
        password = password + random.choice(characters)
    return password

print(password_builder())
