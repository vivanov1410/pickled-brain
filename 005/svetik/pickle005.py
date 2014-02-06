# you can not hide... I... see... you...! (Sauron from "Lords of the Rings")


class TemperatureConverter:

    MINIMUM_TEMPERATURE_IN_FAHRENHEIT = -459.67
    MINIMUM_TEMPERATURE_IN_CELSIUS = -273.15

    @staticmethod
    def is_number(number):
        return type(number) == int

    def to_celsius(self, temperature):
        """Converts temperature to Celsius"""
        if not self.is_number(temperature):
            print('Error. Temperature should be numeric')
            exit()
        elif temperature <= self.MINIMUM_TEMPERATURE_IN_FAHRENHEIT:
            print("Error. The minimum temperature in Fahrenheit is {0}".format(self.MINIMUM_TEMPERATURE_IN_FAHRENHEIT))
            exit()
        else:
            return (temperature - 32) * 5 / 9

    def to_fahrenheit(self, temperature):
        """Converts temperature to Fahrenheit"""
        if not self.is_number(temperature):
            print('Error. Temperature should be numeric')
            exit()
        elif temperature <= self.MINIMUM_TEMPERATURE_IN_CELSIUS:
            print("Error. The minimum temperature in Celsius is {0}".format(self.MINIMUM_TEMPERATURE_IN_CELSIUS))
            exit()
        else:
            return (temperature * 9) / 5 + 32


my_temperature = TemperatureConverter()

print("Temperature in Celsius is {0}".format(my_temperature.to_celsius(232)))
print("Temperature in Fahrenheit is {0}".format(my_temperature.to_fahrenheit(50)))