class Cars:

    def __init__(self):
        self.color = self.color2()
        self.doors = self.doors2()
        self.number_wheels = 4

    def color2(self):
        color = input("What color?: ")
        return color

    def doors2(self):
        doors = input("How many doors?: ")
        return doors

    def honk(self):
        print("honk")


if __name__ == '__main__':
    car1 = Cars()
    print("The color of your car is {} and there are {} doors.".format(car1.color, car1.doors))
