from random import randint

def pick6_lottery():
    n1 = randint(1, 99)
    n2 = randint(1, 99)
    n3 = randint(1, 99)
    n4 = randint(1, 99)
    n5 = randint(1, 99)
    n6 = randint(1, 99)
    return n1, n2, n3, n4, n5, n6


def matching_numbers(user_picks, lottery_picks):

    your_matches = 0

    for i in range(6):
        if user_picks[i] == lottery_picks[i]:
            your_matches += 1
    return your_matches


def earnings():
    your_balance = -2

    if your_matches == 1:
        your_balance += 4
    elif your_matches == 2:
        your_balance += 7
    elif your_matches == 3:
        your_balance += 100
    elif your_matches == 4:
        your_balance += 50000
    elif your_matches == 5:
        your_balance += 1000000
    elif your_matches == 6:
        your_balance += 25000000
    else:
        your_balance += 0
    return your_balance

#
# user_picks = pick6_lottery()
# lottery_picks = pick6_lottery()
# # balance =
# # # winnings = your_balance()
# print(user_picks)
# print(lottery_picks)
# your_matches = matching_numbers(user_picks, lottery_picks)
# print(your_matches)
# balance = earnings()
# print("Your balance after this ticket is: {}".format(balance))

balance = 0
for i in range (100000):
    user_picks = pick6_lottery()
    lottery_picks = pick6_lottery()
    your_matches = matching_numbers(user_picks, lottery_picks)
    balance = balance + earnings()
    print(balance)
