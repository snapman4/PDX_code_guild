chosen_number = input("Choose a number between 0 and 99: ")
chosen_number = int(chosen_number)

tens_digit = chosen_number // 10
ones_digit = chosen_number % 10

# print(tens_digit)
# print(ones_digit)

def tens():
    if tens_digit == 9:
        tens_name = "ninety "
    elif tens_digit == 8:
        tens_name = "eighty "
    elif tens_digit == 7:
        tens_name = "seventy "
    elif tens_digit == 6:
        tens_name = "sixty "
    elif tens_digit == 5:
        tens_name = "fifty "
    elif tens_digit == 4:
        tens_name = "forty "
    elif tens_digit == 3:
        tens_name = "thirty "
    elif tens_digit == 2:
        tens_name = "twenty "
    elif tens_digit == 0:
        tens_name = ""
    elif tens_digit == 1:
        tens_name = ""
    return tens_name
# print(tens())

def ones():
    if ones_digit == 9:
        ones_name = "nine"
    elif ones_digit == 8:
        ones_name = "eight"
    elif ones_digit == 7:
        ones_name = "seven"
    elif ones_digit == 6:
        ones_name = "six"
    elif ones_digit == 5:
        ones_name = "five"
    elif ones_digit == 4:
        ones_name = "four"
    elif ones_digit == 3:
        ones_name = "three"
    elif ones_digit == 2:
        ones_name = "two"
    elif ones_digit == 1:
        ones_name = "one"
    return ones_name
# print(ones())

def teens():
    if chosen_number == 11:
        teen_name = "eleven"
    elif chosen_number == 12:
        teen_name = "twelve"
    elif chosen_number == 13:
        teen_name = "thirteen"
    elif chosen_number == 14:
        teen_name = "fourteen"
    elif chosen_number == 15:
        teen_name = "fifteen"
    elif chosen_number == 16:
        teen_name = "sixteen"
    elif chosen_number == 17:
        teen_name = "seventeen"
    elif chosen_number == 18:
        teen_name = "eighteen"
    elif chosen_number == 19:
        teen_name = "nineteen"
    else:
        teen_name = ""
    return teen_name

teen_num = teens()
tens_num = tens()
ones_num = ones()

if chosen_number >= 10 and chosen_number < 20:
    print(teen_num)
else:
    print(tens_num + ones_num)

# print(teen_num + tens_num + ones_num)
