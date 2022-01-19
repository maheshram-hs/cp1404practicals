from prac_08.car import Car
import random


class UnreliableCar(Car):
    """..."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(1, 100) >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)  # super(UnreliableCar, self).drive(distance) Will this work?
        return drive_distance
