import math
def wall_measurements():
    width = int(input("How wide is the wall you're painting (in feet)?: "))
    height = int(input("How tall is the wall (in feet)?: "))
    total_space = (width * height)
    return total_space
total_space = wall_measurements()
print("The square footage you are looking at painting is {}".format(total_space))


def paint_cost():
    paint = float(input("How much does a gallon of paint cost?: "))
    return paint

paint = paint_cost()

def number_cans_needed():
    amount_of_paint = math.ceil(total_space / 400)
    return amount_of_paint

number_cans = number_cans_needed()
print("You will need {} cans of paint".format(number_cans))
total_cost = number_cans * paint
print("{} can(s) of paint will cost you ${}.".format(number_cans, total_cost))
#print(number_cans_needed())

# def project_cost():
#     overall_cost = (total_space / 400) * paint
#     return overall_cost
#
# print("The project will cost you ${} to paint one coat.".format(project_cost()))

# def muliple_coats():
#     multiple = input("Are you going to use multiple coats of paint? yes/no: ")
#     if multiple == "yes".lower():
#         how_many = int(input("How many coats?: "))
#         multiple = how_many * project_cost()
#         return multiple
#         print("{} many coats will cost you ${}.".format(how_many, multiple))
#     else:
#          print("well nevermind then.")
#
# print("The project should cost you ${} in total.".format(muliple_coats()))
