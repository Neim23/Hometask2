import random


class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100  # Початковий капітал
        self.progress = 0  # Рівень знань
        self.gladness = 50  # Рівень щастя
        self.alive = True

    def to_study(self):
        print("Час вчитися!")
        self.progress += 5
        self.gladness -= 3

    def to_sleep(self):
        print("Студент спить... zZz")
        self.gladness += 2

    def to_chill(self):
        print("Час відпочинку!")
        self.gladness += 5
        self.progress -= 1
        self.money -= 20  # Відпочинок коштує грошей

    def to_work(self):
        print("Йдемо на роботу, щоб вижити.")
        self.money += 50
        self.gladness -= 4
        self.progress -= 2

    def is_alive(self):
        if self.progress < -5:
            print("Відраховано...")
            self.alive = False
        elif self.gladness <= 0:
            print("Депресія...")
            self.alive = False
        elif self.money < -50:
            print("Банкрут...")
            self.alive = False

    def end_of_day(self):
        print(f"Щастя: {self.gladness}, Знання: {self.progress}, Гроші: {self.money}")

    def live(self, day):
        day_str = f" День {day} з життя {self.name} "
        print(f"{day_str:=^40}")

        # Логіка прийняття рішень
        if self.money < 30:
            self.to_work()
        elif self.progress < 5:
            self.to_study()
        elif self.gladness < 15:
            self.to_chill()
        else:
            # Якщо все в нормі — випадкова дія
            choice = random.randint(1, 3)
            if choice == 1:
                self.to_study()
            elif choice == 2:
                self.to_chill()
            elif choice == 3:
                self.to_sleep()

        self.is_alive()
        self.end_of_day()


# --- Запуск симуляції на 365 днів ---
nick = Student(name="Микола")

for day in range(1, 366):
    if nick.alive == False:
        break
    nick.live(day)