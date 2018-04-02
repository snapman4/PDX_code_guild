from random import choice

eyes = ["8", "B", ":", ";"]
nose = ["o", "*", "^"]
mouth = [")", "(", "D", "P", ">"]

counter = 0
while counter < 5:
    print(choice(eyes) + choice(nose) + choice(mouth))
    counter = counter + 1
