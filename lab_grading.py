grade = int(input("What percentage did you get in the course?: "))
grade_adjustment = grade % 10

if grade_adjustment <= 3:
    grade_adjustment = "-"
elif grade_adjustment >= 7:
    grade_adjustment = "+"

if grade >= 93:
    print("You got an A")
elif grade >= 90:
    print("You got an A" + grade_adjustment)
elif grade >= 80:
    print("You got a B" + grade_adjustment)
elif grade >= 70:
    print("You got a C" + grade_adjustment)
elif grade >= 60:
    print("You got a D" + grade_adjustment)
else:
    print("You got an F")
