def change_input():
    how_much = float(input("How much change are you getting back?: "))
    return how_much

change_input = change_input()


def convert_to_coin():
    cash_on_hand = change_input * 100
    return cash_on_hand

cash = convert_to_coin()


def dispense_change():
    hundreds = round(cash // 10000)
    remainder = cash % 10000
    fifties = round(remainder // 5000)
    remainder = remainder % 5000
    twenties = round(remainder // 2000)
    remainder = remainder % 2000
    tens = round(remainder // 1000)
    remainder = remainder % 1000
    fives = round(remainder // 500)
    remainder = remainder % 500
    ones = round(remainder // 100)
    remainder = remainder % 100
    quarters = round(remainder // 25)
    remainder = remainder % 25
    dimes = round(remainder // 10)
    remainder = remainder % 10
    nickels = round(remainder // 5)
    remainder = remainder % 5
    pennies = round(remainder // 1)
    return hundreds, fifties, twenties, tens, fives, ones, quarters, dimes, nickels, pennies


hundreds, fifties, twenties, tens, fives, ones, quarters, dimes, nickels, pennies = dispense_change()

print("You will get: \n {} hundreds \n {} fifties \n {} twenties \n {} tens \n {} fives \n {} ones \n {} quarters \n {} dimes \n {} nickels \n {} pennies".format(hundreds, fifties, twenties, tens, fives, ones, quarters, dimes, nickels, pennies))
(dispense_change())

#  TUPLE UNPACKING EXAMPLE BELOW
# def gather_information():
#     from_meas = input("What measurement do you want to convert from?: ")
#     amount = float(input("What is the amount you want to convert?: "))
#     to_meas = input("What measurement do you want to convert to?: ")
#     return from_meas, to_meas, amount
# print("Welcome to the super cool distance converter.")
# While True:
#     frm, to, amount = gather_information() #tuple unpacking
