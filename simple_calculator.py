# Let’s write a simple REPL (read evaluate print loop) calculator that can
#handle addition, subtraction, multiplication, and division.
#Ask the user for an operator and each operand. Don’t forget that input returns
#a string, which you can convert to a float using float(user_input)
#where user_input is the string you got from input.
#Below is some sample input/output.
#
# > What is the operation you'd like to perform? +
# > What is the first number? 5
# > What is the second number? 12
# > 5 + 12 = 17


type_calc = input("What is the operation you'd like to perform? [+] [-] [/] [*]: ")
first_num = int(input("What is the first number?: "))
second_num = int(input("What is the second number?: "))
print("Ok, here's your answer... {} {} {} equals: ".format(first_num, type_calc, second_num))

def calculation():
    if type_calc == "+":
        math = first_num + second_num
    elif type_calc == "-":
        math =  first_num - second_num
    elif type_calc == "/":
        math = first_num / second_num
    elif type_calc == "*":
        math = first_num * second_num
    else:
        math = "I don't know that type of equation."
    return math
print(calculation())
