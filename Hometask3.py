import random


class House:
    def __init__(self):
        self.food = 50  # Кількість їжі в холодильнику
        self.mess = 0  # Рівень безладу в домі

    def __str__(self):
        return f"Стан дому: Їжа = {self.food}, Безлад = {self.mess}"


class Sim:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 50
        self.energy = 50
        self.money = 100

    def eat(self):
        if self.house.food >= 10:
            print(f"{self.name} поїв(ла).")
            self.fullness += 20
            self.house.food -= 10
        else:
            print(f"В домі немає їжі! {self.name} йде в магазин.")
            self.shopping()

    def work(self):
        print(f"{self.name} сходив(ла) на роботу.")
        self.money += 50
        self.fullness -= 10
        self.energy -= 20

    def shopping(self):
        if self.money >= 20:
            print(f"{self.name} купив(ла) продукти.")
            self.money -= 20
            self.house.food += 30
        else:
            print("Немає грошей на їжу! Треба працювати.")
    def sleep(self):
        print(f"{self.name} спить.")
        self.energy += 40
        self.fullness -= 5
    def live_day(self, day_number):
        print(f"--- День {day_number} для {self.name} ---")
        if self.fullness < 20:
            self.eat()
        elif self.energy < 20:
            self.sleep()
        elif self.money < 30:
            self.work()
        else:
            action = random.choice(["work", "eat", "sleep"])
            getattr(self, action)()
        print(f"Статус: Ситість={self.fullness}, Енергія={self.energy}, Гроші={self.money}")
        print(self.house)
        print("-" * 30)
my_house = House()
my_sim = Sim("Миколи", my_house)
for day in range(1, 6):
    my_sim.live_day(day)