# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

def enter_cc():
    return input("Please enter a valid 16 digit credit card number: ")

cc = enter_cc()


cc_num = []
for i in range(len(cc)):
    cc_num.append(int(cc[i])) #turns this into a list of the integers

# print(cc_num)
popped = cc_num.pop(-1)
# print(cc_num)
cc_num.reverse()
# print(cc_num)
for i in range(len(cc_num)):  #this takes the number of integers as i
    if i % 2 == 0:
        cc_num[i] *= 2
# print(cc_num)
for i in range(len(cc_num)): #this takes the number of integers as i
    if cc_num[i] > 9:
        cc_num[i] -= 9
# print(cc_num)
# print(popped)
ccsum = sum(cc_num)
# print(ccsum)
last_digit = ccsum % 10
# print(last_digit)
if popped == last_digit:
    print("Verified")
else:
    print("invalid")
# mess with this line below
# for i range(len(cc_num)):
#     if i % 2 == 0:
#         cc_num[i] *= 2
