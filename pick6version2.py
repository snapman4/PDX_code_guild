from random import randint

def pick6_lottery():
    n1 = randint(1,99)
    n2 = randint(1,99)
    n3 = randint(1,99)
    n4 = randint(1,99)
    n5 = randint(1,99)
    n6 = randint(1,99)
    return n1, n2, n3, n4, n5, n6

n1, n2, n3, n4, n5, n6 = pick6_lottery()


def user_picks():
    up1 = randint(1,99)
    up2 = randint(1,99)
    up3 = randint(1,99)
    up4 = randint(1,99)
    up5 = randint(1,99)
    up6 = randint(1,99)
    return up1, up2, up3, up4, up5, up6

up1, up2, up3, up4, up5, up6 = user_picks()

matching_numbers = 0

def number_matches(pick6_lottery, user_picks):

    if n1 == up1:
        matching_numbers += 1
    if n2 == up2:
        matching_numbers += 1
    if n3 == up3:
        matching_numbers += 1
    if n4 == up4:
        matching_numbers += 1
    if n5 == up5:
        matching_numbers += 1
    if n6 == up6:
        matching_numbers += 1
    return matching_numbers


def matching():
    if matching_numbers == 0:
        winnings = 0
    elif matching_numbers == 1:
        winnings = 4
    elif matching_numbers == 2:
        winnings = 7
    elif matching_numbers == 3:
        winnings = 100
    elif matching_numbers == 4:
        winnings = 50000
    elif matching_numbers == 5:
        winnings = 1000000
    elif matching_numbers == 6:
        winnings = 25000000
    return winnings


for i in range (1000):
    (user_picks())
    (pick6_lottery())
    # total_balance = -2 + winnings
    print("Matching numbers in this draw. {} ".format(matching_numbers))
    # print("winnings so far {} ".format(winnings))
    # print(total_balance)
