def enter_cc():
    return input("Please enter a valid 16 digit credit card number: ")

cc = enter_cc()

def turn_to_int():
    cc_num = []
    for i in range(len(cc)):
        cc_num.append(int(cc[i]))
    return cc_num
# print(turn_to_int())
print(cc_num)

def remove_last():
    popped = cc_num.pop(-1)
    return popped
    return cc_num


def reverse_list():
    cc_num.reverse()
    return cc_num


def mult_even_by_two():
    for i in range(len(cc_num)):
        if i % 2 == 0:
            cc_num[i] *= 2
    return cc_num

def subtract9():
    for i in range(len(cc_num)):
        if cc_num[i] > 9:
            cc_num[i] -= 9
    return cc_num

def credit_num_sum():
    ccsum = sum(cc_num)
    return ccsum

def last_num():
    last_digit = ccsum % 10
    return last_digit

def combining():
    turn_to_int()
    remove_last()
    # reverse_list()
    # mult_even_by_two()
    # subtract9()
    # credit_num_sum()
    # last_num()
    #
    # if popped == last_digit:
    #     return verified
    # else:
    #     return invalid

print(combining())
