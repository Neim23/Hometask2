import random


class Encryptor:
    def __init__(self, *args):
        self.__numbers = list(args)
        self.__result = 0
        self.__calculate()

    def __calculate(self):
        """Проводить випадкову математичну операцію над кожним числом."""
        for num in self.__numbers:
            operation = random.choice(['add', 'sub', 'mul'])
            rand_val = random.randint(1, 10)

            if operation == 'add':
                self.__result += (num + rand_val)
            elif operation == 'sub':
                self.__result += (num - rand_val)
            elif operation == 'mul':
                self.__result += (num * rand_val)

    def __str__(self):
        return f"Результат обчислень: {self.__result}"


crypto = Encryptor(10, 20, 30)
print(crypto)
