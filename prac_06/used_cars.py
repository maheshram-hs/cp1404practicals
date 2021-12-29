"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)  # fuel: 150

    print("\n* Car *\n")

    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(f"\n{my_car}")

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print("\n* Limo *\n")

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"fuel: {limo.fuel}")
    limo.drive(115)
    print(f"odo: {limo.odometer}")  # fuel: 5
    print(limo)


if __name__ == '__main__':
    main()
