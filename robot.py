
class Robot:

    # read population from file ...
    population_robots = 0  # class members (static)

    def __init__(self, name):
        self.name = name
        Robot.population_robots += 1

    def introduce(self):
        print(f"Hi I am {self.name}")

    # static method vs class method
    # static method does not approach static fields
    # only class method

    @classmethod
    def reach_10(cls):
        # return Robot.population_robots >= 10
        return cls.population_robots >= 10

    @staticmethod
    def is_legal_name(name):
        return len(name) > 2 and name.isalpah()

class MiniRobot(Robot):
    def foo(self):
        print(Robot.reach_10())  # better
        print(self.reach_10())  # works but BAD
        print(super().reach_10())  # works but BAD

print(Robot.population_robots)  # 0

r = Robot('THREEPO')

print(Robot.population_robots)  # 1