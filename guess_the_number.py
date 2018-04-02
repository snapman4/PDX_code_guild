from random import randint

x = randint(1,100)
# print(x) will give you the random computer number

counter = 0
while counter <  10:

    user_guess = input("Guess the number between 1 and 100: ")
    if int(user_guess) == x:
        print("Correct!")
        break
    elif int(user_guess) > x:
        counter = counter + 1
        print("Nope, too high, guess again")
    elif int(user_guess) < x:
        counter = counter + 1
        print("Nope, too low, guess again")
    else:
        print("better luck next time")

print("You guessed {} times".format(counter + 1))
