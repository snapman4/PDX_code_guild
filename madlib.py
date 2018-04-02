# **Four** score and **seven** **years** ago our **fathers** brought forth,
# upon this **continent**, a new nation, **conceived** in **liberty**,
# and dedicated to the **proposition** that all **men** are created **equal**.

time1 = input("Give me a number: ")
time2 = input("Give me another number: ")
length = input("What's a length of time: ")
noun1 = input("Give me a noun: ")
place = input("Give me a place: ")
verb1 = input("Give me a verb: ")
noun2 = input("Give me another noun: ")
noun3 = input("How about another noun: ")
person = input("Give me a person: ")
adjective = input("Give me an adjective: ")

madlib = ("""
{} score and {} {} ago our {} brought forth, upon this {},
a new nation, {} in {}, and dedicated to the {}
that all {} are created {}. """.format(time1, time2, length, noun1, place, verb1, noun2, noun3, person, adjective))
madlib_answer = input("Do you want to hear your madlib? ")
if madlib_answer.lower() == "yes":
    print(madlib)
try_again = input("Do you want to try again?: yes/no? ")

while try_again.lower() == "yes":
    time1 = input("Give me a number: ")
    time2 = input("Give me another number: ")
    length = input("What's a length of time: ")
    noun1 = input("Give me a noun: ")
    place = input("Give me a place: ")
    verb1 = input("Give me a verb: ")
    noun2 = input("Give me another noun: ")
    noun3 = input("How about another noun: ")
    person = input("Give me a person: ")
    adjective = input("Give me an adjective: ")

    madlib = ("""
    {} score and {} {} ago our {} brought forth, upon this {},
    a new nation, {} in {}, and dedicated to the {}
    that all {} are created {}. """.format(time1, time2, length, noun1, place, verb1, noun2, noun3, person, adjective))

    print(madlib)

    if try_again.lower() == "no":
        break




#print(time1 + " score and " time2 + " " + length + " ago our " + noun1 + " brought forth, upon this " + place + ", \n a new nation, " + verb1 + " in " + noun2 + ", and dedicated to the " + noun3 + " \n that all " + person + " are created " + adjective + ".")
