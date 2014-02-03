# there is no life in the void...only...death... (Sauron from "Lords of the Rings")
class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type

    def is_number(self, number):
        return type(number) == int

    readings = []

    def add(self, reading):
        if not self.is_number(reading):
            return "error"
        self.readings.append(reading)

    def reset(self):
        self.readings = []

    def average(self):
        return sum(self.readings) / len(self.readings)

    def smallest(self):
        return min(self.readings)

    def biggest(self):
        return max(self.readings)


my_sensor = Sensor("temperature")
print(my_sensor.sensor_type)

my_sensor.add(10)
my_sensor.add(15)
my_sensor.add(5)
print(my_sensor.readings)

print(my_sensor.smallest())

print(my_sensor.biggest())

print(my_sensor.average())