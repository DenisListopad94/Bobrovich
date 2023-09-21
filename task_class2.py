# 1. Определить класс «Шахматная фигура» с ее координатами на шахматной доске, ее цветом (черный или белый),
# виртуальным методом «битья» другой фигуры, и унаследовать от него классы,
# соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь». Написать виртуальные методы «битья» другой фигуры,
# которые принимают координаты другой фигуры и определяют,
# может ли данная фигура «бить» фигуру с теми (принятыми) координатами.

class ChessFigure:
    def __init__(self, x: int, y: int, color: str, name: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = name


class Queen(ChessFigure):
    def fig_hit(self):
        while True:
            x1, y1 = map(int, input(f"Введите через пробел координаты хода фигуры '{self.name}' 'x1' и 'y1':").split())
            if abs(self.x - x1) == abs(self.y - y1) or self.x == x1 or self.y == y1:
                x = x1
                y = y1
                print(f"Координаты фигуры '{self.color} {self.name}' после боя стали x = {x}, y = {y} ")
                if x == some_fig.x and y == some_fig.y:
                    print(f"Ваша фигура '{self.name}' побила фигуру '{some_fig.name}'")
                break
            else:
                print(f"Так фигура '{self.color} {self.name}' бить не может, укажите другие координаты")


class Pawn(ChessFigure):
    def fig_hit(self):
        while True:
            x1, y1 = map(int, input(f"Введите через пробел координаты хода фигуры '{self.name}' 'x1' и 'y1':").split())
            if (x1 == self.x + 1 or x1 == self.x - 1) and y1 == self.y + 1 and x1 == some_fig.x and y1 == some_fig.y:
                x = x1
                y = y1
                print(f"Координаты фигуры '{self.color} {self.name}' после боя стали x = {x}, y = {y} ")
                print(f"Ваша фигура '{self.name}' побила фигуру '{some_fig.name}'")
                break
            if x1 == self.x and y1 == self.y + 1:
                x = x1
                y = y1
                print(f"Координаты фигуры '{self.color} {self.name}' после хода стали x = {x}, y = {y} ")
                break
            else:
                print(f"Так фигура '{self.color} {self.name}' бить не может, укажите другие координаты")


class Horse(ChessFigure):
    def fig_hit(self):
        while True:
            x1, y1 = map(int, input(f"Введите через пробел координаты хода фигуры '{self.name}' 'x1' и 'y1':").split())
            if (self.x - 1 == x1 or self.x + 1 == x1) and (self.y - 2 == y1 or self.y + 2 == y1):
                x = x1
                y = y1
                print(f"Координаты фигуры '{self.color} {self.name}' после боя стали x = {x}, y = {y} ")
                if x == some_fig.x and y == some_fig.y:
                    print(f"Ваша фигура '{self.name}' побила фигуру '{some_fig.name}'")
                break
            elif (self.x - 2 == x1 or self.x + 2 == x1) and (self.y - 1 == y1 or self.y + 1 == y1):
                x = x1
                y = y1
                print(f"Координаты фигуры '{self.color} {self.name}' после боя стали x = {x}, y = {y} ")
                if x == some_fig.x and y == some_fig.y:
                    print(f"Ваша фигура '{self.name}' побила фигуру '{some_fig.name}'")
            else:
                print(f"Так фигура '{self.color} {self.name}' бить не может, укажите другие координаты")


some_fig = ChessFigure(4, 3, "white", "pawn")
queen = Queen(6, 1, "black", "queen")
pawn = Pawn(2, 4, "black", "pawn")
horse = Horse(3, 1, "black", "horse")
queen.fig_hit()  # 4 3
pawn.fig_hit()   # 2 5
horse.fig_hit()  # 4 3

# 2. Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль».
# Определить время и стоимость перевозки для указанных городов и расстояний


class Transporter:

    def __init__(self, city1: str, city2: str, distance: int):
        self.city1 = city1
        self.city2 = city2
        self.distance = distance

    def travel_time(self, average_speed: int):
        self.average_speed = average_speed
        time = self.distance / self.average_speed
        return time

    def price_delivery(self, price_1km: int):
        self.price_1km = price_1km
        price = self.price_1km * self.distance
        return price


class Plane(Transporter):
    def info(self):
        print(f"Время грузоперевозки самолетом из {self.city1} в {self.city2} составит {super().travel_time(300)} ч.")
        print(f"Стоимость - {super().price_delivery(10)} EUR")


class Trane(Transporter):
    def info(self):
        print(f"Время грузоперевозки поездом из {self.city1} в {self.city2} составит {super().travel_time(50)} ч.")
        print(f"Стоимость - {super().price_delivery(2)} EUR")


class Vehicle(Transporter):
    def info(self):
        print(f"Время грузоперевозки автомобилем из {self.city1} в {self.city2} составит {super().travel_time(80)} ч.")
        print(f"Стоимость - {super().price_delivery(5)} EUR")


plane = Plane("Minsk", "Warsaw", 600)
trane = Trane("Minsk", "Warsaw", 600)
vehicle = Vehicle("Minsk", "Warsaw", 600)
plane.info()
trane.info()
vehicle.info()

# 3. Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
# Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
# Представитель каждого класса может умереть, если достигнет определенного возраста или для него не будет еды.
# Напишите виртуальные методы поедания и определения состояния живого существа
# (живой или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).

class Live:

    def __init__(self, name: str, age: int, food=True):
        self.name = name
        self.age = age
        self.food = food

class Fox(Live):

    def status(self):
        if self.age >= 9:
            print(f"Лиса {self.name} сдохла от старости :(")
        elif self.food is not True:
            print(f"Лиса {self.name} сдохла от голода :(")
        else:
            print(f"Лиса {self.name} съела кролика и довольная гуляет :)")

class Rabbit(Live):

    def status(self):
        if self.age >= 4:
            print(f"Кролик {self.name} сдох от старости :(")
        elif self.food is not True:
            print(f"Кролик {self.name} сдох от голода :(")
        else:
            print(f"Кролик {self.name} съел растение и довольный гуляет :)")

class Herb(Live):

    def status(self):
        if self.age >= 3:
            print(f"Растение {self.name} высохло от старости :(")
        elif self.food is not True:
            print(f"Растение {self.name} высохло от отсутствия солнечного света :(")
        else:
            print(f"Растение {self.name} насытилось солнцем и радостно зеленеет :)")

fox1 = Fox("Fox1", 5)
fox2 = Fox("Fox2", 9)
fox3 = Fox("Fox3", 6, False)
fox1.status()
fox2.status()
fox3.status()
rabbit1 = Rabbit("Rabbit1", 2, False)
rabbit2 = Rabbit("Rabbit2", 3)
rabbit3 = Rabbit("Rabbit3", 5)
rabbit1.status()
rabbit2.status()
rabbit3.status()
herb1 = Herb("Herb1", 3)
herb2 = Herb("Herb2", 2)
herb3 = Herb("Herb3", 3, False)
herb1.status()
herb2.status()
herb3.status()
