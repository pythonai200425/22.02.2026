

class Circle:

    pie = 3.14  # can access without creating instance

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @staticmethod
    def how_calc_hekef():
        return "2 * pi * r"

    @classmethod
    def foo(cls):
        print(cls.how_calc_hekef())

    def get_hekef(self):
        return 2 * Circle.pie * self.radius

print(Circle.pie)
print(Circle.how_calc_hekef())

c = Circle(3.4)
print(c.get_hekef())
c1 = Circle(3.4)
c2 = Circle(3.4)

c1.pie = 3.15
c2.pie = 3.15
c.pie = 3.15
print(c.how_calc_hekef())
