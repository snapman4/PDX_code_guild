def bad_number():
    dirty_number = input("Please enter your ten digit phone number with no spaces or special characters: ")
    return dirty_number

dirty_number = bad_number()

def option1():
    clean_phone = dirty_number[0:3] + "-" + dirty_number[3:6] + "-" + dirty_number[6:]
    return clean_phone

print(option1())
print("or")


def option2():
    clean_phone2 = "(" + dirty_number[0:3] + ") " + dirty_number[3:6] + "-" + dirty_number[6:]
    return clean_phone2

print(option2())

#code practicing below for proper code above
# def phone_number():
#     # dirty_number = input("Please enter your ten digit phone number with no spaces or special characters: ")
#     dirty_number = "(" + dirty_number[0:3] + ") " + dirty_number[3:6] + "-" + dirty_number[6:]
#     return dirty_number
#     other_dirty_number = dirty_number[0:3] + "-" + dirty_number[3:6] + "-" + dirty_number[6:]
#
#     return other_dirty_number
#
# dirty_number = phone_number()
# # print("or")
# print(phone_number())
