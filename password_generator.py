from random import choice
import string


# #def all_characters():
# def length_pw():
#     return input("How many characters would you like in your password?: ")
#
#
# def compile_pw(password):
#     password_characters = string.printable
#     password = ' '
#     for i in range (0, int(length_pw)):
#         password = password + random.choice(password_characters)
#         return str(password)
#
#
# (length_pw())

# def random_password():
#     password_characters = string.printable
#     pw_length = input("How many password characters would you like?: ")
#     password = ' '
#     for i in range (0, int(pw_length)):
#         password = password + choice(password_characters)
#         #return str(password)
# (random_password())
#

# #password_generator.py
# import string
# import random
# password_characters = string.printable
# length = input("Number of password characters desired: ")
# password = ''
# for i in range (0, int(length)):
#     password = password + random.choice(password_characters)
# print(password)


# def password_generator(password, length):
#
#     list_of_char = string.printable
#     pw_length = input("How many characters do you want for your password: ")
#     pw = " "
#     for i in range(int(pw_length)):
#         pw = pw + random.choice(list_of_char)
#     return pw

def password_generator(password):
    import string
    import random
    password_characters = string.printable
    length = input("Number of password characters desired: ")
    password = ''
    for i in range (0, int(length)):
        password = password + random.choice(password_characters)
print(length)
