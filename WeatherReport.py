
class WeatherReport:
    fahr_minus_number = 32
    fahr_fraction = 5/9

    to_fahr_mul = 1.8
    to_fahr_add = 32

    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return WeatherReport.from_celcius_to_fahrenheit(self.celsius)

    # 1
    # return true if temp above 40 or below 0
    @staticmethod
    def is_extreme(temp_celcius):
        return temp_celcius < 0 or temp_celcius > 40

    # 2
    def display(self):
        "show this report temperatrue in celcius and fahrenit"
        print(f"Temperature {self.celsius}°C  {WeatherReport.from_celcius_to_fahrenheit(self.celsius)}°F")
        print(f"Temperature {self.celsius}°C  {self.fahrenheit}°F")

    # 3) convert F to C
    # Formula: (F - 32) * 5/9
    @classmethod
    def from_fahrenheit_to_celcius(cls, f_value):
        return (f_value - cls.fahr_minus_number) * cls.fahr_fraction

    # 4) convert C to F
    # (°C × 1.8) + 32
    def from_celcius_to_fahrenheit(c_value):
        "return fahrenheit"
        pass