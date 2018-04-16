class Car:
    def __init__(self, color, number_of_doors):
        self.number_of_wheels = 4
        self.color = color
        self.number_of_doors = number_of_doors

    def honk(self):
        print('honk')


import car

def main():
    car_one = car.Car('black', 4)
    car_two = car.Car('black', 4)
    car_three = car.Car('blue', 4)
    car_four = car.Car('brown', 2)

    lst_of_cars = [car_one, car_two, car_three, car_four]

    for vehicle in lst_of_cars:
        print(vehicle.color)
        print(vehicle.number_of_doors)
        print(vehicle.number_of_wheels)
        vehicle.honk()
        print('-'* 46)


if __name__ == '__main__':
    main()