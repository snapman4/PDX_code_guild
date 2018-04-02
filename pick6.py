from random import randint
for i in range(5):
    matching_numbers = 0
    lottery_balance = 0
    winnings = 0
    total_balance = 0

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

    # print("The correct numbers are: {}, {}, {}, {}, {}, {}".format(n1, n2, n3, n4, n5, n6))
    # print("Your lottery numbers are: {}, {}, {}, {}, {}, {}".format(up1, up2, up3, up4, up5, up6))
#print(up1, up2)
#user_ticket = up1, up2, up3, up4, up5, up6

    if n1 == up1:
        matching_numbers = matching_numbers + 1
    if n2 == up2:
        matching_numbers = matching_numbers + 1
    if n3 == up3:
        matching_numbers = matching_numbers + 1
    if n4 == up4:
        matching_numbers = matching_numbers + 1
    if n5 == up5:
        matching_numbers = matching_numbers + 1
    if n6 == up6:
        matching_numbers = matching_numbers + 1

    # print(matching_numbers)
    # print(your_balance)

    if matching_numbers == 0:
        winnings -= 2
    elif matching_numbers == 1:
        winnings += 4
    elif matching_numbers == 2:
        winnings += 7
    elif matching_numbers == 3:
        winnings += 100
    elif matching_numbers == 4:
        winnings += 50000
    elif matching_numbers == 5:
        winnings += 1000000
    elif matching_numbers == 6:
        winnings += 25000000

    total_balance = total_balance + winnings

    # total_balance = your_balance += your_balance
    # print("Your numbers: {}, the actual numbers: {}".format(user_picks(), pick6_lottery()))
    print("Matching numbers: {}".format(matching_numbers))
    # print("Your balance is: {}".format(total_balance))
    print(winnings)
    print(total_balance)
