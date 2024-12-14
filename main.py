import random
class NumberHided:
    def __init__(self, number):
        self.__number = number
        self.__result = None
    def __random_operation(self):
        operation = random.choice(["add", "subtract", "multiply", "divide"])
        random_value = random.randint(1, 10)
        if operation == "add":
            self.__result = self.__number + random_value
        elif operation == "subtract":
            self.__result = self.__number - random_value
        elif operation == "multiply":
            self.__result = self.__number * random_value
        elif operation == "divide":
            self.__result = round(self.__number / random_value, 2)
    def __str__(self):
        if self.__result is None:
            self.__random_operation()
        return f"Результат шифрування числа: {self.__result}"
NumberHided1 = NumberHided(5)
NumberHided2 = NumberHided(2)
print(NumberHided1)
print(NumberHided2)
