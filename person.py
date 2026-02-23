class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create object function
    # possible but not efficient
    @classmethod
    def create_person(cls, name, age):
        return Person(name, age)

    # possible but not efficient
    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split(",")
        # return Person(name, age)
        return cls(name, age)


    def __str__(self):
        return f"Person [name]:{self.name} [age]:{self.age}"

p1 = Person("Alice", 30)
print(p1)
p2 = Person.create_person("Alice", 30)
print(p2)
p3 = Person.from_string("Alice,30")
print(p3)
data = input("describe person?")
p4 = Person.from_string(data)
print(p4)