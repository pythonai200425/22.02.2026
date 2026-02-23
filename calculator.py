

# static methods , class methods

class Calculator:

    # access functions without creating an instance

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

# calc = Calculator()  3 without instance
print(Calculator.add(3, 4))
print(f"19 even? {Calculator.is_even(19)}")

c = Calculator()


class UserValidator:
    # is_valid_email(email) --> return true if @ and . inside the email
    # is_strong_password(password) --> return true if len >= 8
    pass

print(UserValidator.is_valid_email("test@gmail.com"))
print(UserValidator.is_strong_password("12345678"))
