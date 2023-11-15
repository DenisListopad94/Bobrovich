# 1. Дан код. Исправить его в соответствии с принципом DRY.
# import sqlite3
# conn1 = sqlite3.connect('database1.db')
# cursor1 = conn1.cursor()
# cursor1.execute('SELECT name FROM users')
# users1 = cursor1.fetchall()
# conn1.close()
# conn2 = sqlite3.connect('database2.db')
# cursor2 = conn2.cursor()
# cursor2.execute('SELECT name FROM customers')
# customers2 = cursor2.fetchall()
# conn2.close()

import sqlite3


def sql_connect(database: str):
    conn = sqlite3.connect(database)
    return conn


cursor1 = sql_connect("database1.db").cursor()
cursor1.execute("SELECT name FROM users")
users = cursor1.fetchall()
sql_connect("database1.db").close()

cursor2 = sql_connect("database2.db").cursor()
cursor2.execute("SELECT name FROM customers")
customers = cursor2.fetchall()
sql_connect("database2.db").close()

# 2. Дан код. Исправить его в соответствии с принципом KISS.

# def calculate_complex_formula(a, b, c, d, e, f, g, h):
#     result = 0
#     if a > 0:
#         result += b * c
#     else:
#         result -= d / e
#     if g < h:
#         result += f * (g + h)
#     else:
#         result -= (d - f) / g
#     return result


def calculate_complex_formula(a, b, c, d, e, f, g, h):
    result = 0
    if a > 0:
        result += b * c
    elif a <= 0:
        result -= d / e
    elif g < h:
        result += f * (g + h)
    else:
        result -= (d - f) / g
    return result

# 3. Дан код. Исправить его в соответствии с принципом POLA.

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         if self.age >= 18:
#             print(f"Привет, {self.name}! Добро пожаловать на сайт для взрослых.")
#         else:
#             print(f"Привет, {self.name}! Добро пожаловать на детский сайт.")
# user1 = User("Алекс", 25)
# user1.greet()
#
# user2 = User("Лиза", 12)
# user2.greet()


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Greet(User):
    def greet(self):
        if self.age >= 18:
            print(f"Привет, {self.name}! Добро пожаловать на сайт для взрослых.")
        else:
            print(f"Привет, {self.name}! Добро пожаловать на детский сайт.")


Greet("Алекс", 25).greet()
Greet("Лиза", 12).greet()

# 4. Дан код. Исправить его в соответствии с принципом Single Responsibility.

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def save_to_database(self):
#         pass
#
#     def send_email(self, message):
#         pass
#
#     def log_activity(self, activity):
#         pass


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SaveToDatabase:
    def save_to_database(self):
        pass


class SendEmail:
    def send_email(self, message):
        pass


class LogActivity:
    def log_activity(self, activity):
        pass

# 5. Дан код. Исправить его в соответствии с принципом Open/Closed.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class AreaCalculator:
#     def calculate_area(self, shape):
#         if isinstance(shape, Rectangle):
#             return shape.width * shape.height
#         elif isinstance(shape, Circle):
#             return 3.14 * shape.radius ** 2
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
# rectangle = Rectangle(5, 4)
# circle = Circle(3)
#
# calculator = AreaCalculator()
#
# area1 = calculator.calculate_area(rectangle)  прямоугольника
# area2 = calculator.calculate_area(circle)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2

# произведем кастомизацию, если нет необходимости высчитывать все площади, а только одну:


class AreaRectangle(Rectangle):
    def calc_area_rectangle(self):
        return self.width * self.height


class AreaCircle(Circle):
    def calc_area_circle(self):
        return 3.14 * self.radius ** 2


# before customisation:

rectangle = Rectangle(5, 4)
print(rectangle)
circle = Circle(3)
print(circle)

calculator = AreaCalculator()

area1 = calculator.calculate_area(rectangle)
area2 = calculator.calculate_area(circle)

print(area1)
print(area2)

# after customisation:

area_rectangle_custom = AreaRectangle(4, 10).calc_area_rectangle()
area_circle_custom = AreaCircle(10).calc_area_circle()

print(area_rectangle_custom)
print(area_circle_custom)

# 6. Дан код. Исправить его в соответствии с принципом Liskov Substitution.

# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         super().__init__(name)
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class AreaCalculator:
#     def calculate_area(self, shape):
#         if isinstance(shape, Shape):
#             return shape.area()
#         else:
#             raise ValueError("Неверный объект фигуры")
#
# rectangle = Rectangle("Прямоугольник", 4, 6)
# circle = Circle("Круг", 3)
#
# calculator = AreaCalculator()
# area1 = calculator.calculate_area(rectangle)
# area2 = calculator.calculate_area(circle)
#
# print(f"{rectangle.name} имеет площадь {area1}")
# print(f"{circle.name} имеет площадь {area2}")


class Shape:
    def __init__(self, name, width=0, height=0, radius=0):
        self.name = name
        self.width = width
        self.height = height
        self.radius = radius

    def area(self):
        pass

    # def area(self):
    #     if self.name == "Прямоугольник":
    #         return self.width * self.height
    #     if self.name == "Круг":
    #         return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name, width, height)

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Shape):
            return shape.area()
        else:
            raise ValueError("Неверный объект фигуры")


rectangle = Rectangle("Прямоугольник", 4, 6)
circle = Circle("Круг", 3)
shape1 = Shape("Круг", radius=5)

calculator = AreaCalculator()
area1 = calculator.calculate_area(rectangle)
area2 = calculator.calculate_area(circle)
area3 = calculator.calculate_area(shape1)

print(f"{rectangle.name} имеет площадь {area1}")
print(f"{circle.name} имеет площадь {area2}")
print(f"{shape1.name} имеет площадь {area3}")

# 7. Дан код. Исправить его в соответствии с принципом Interface Segregation.

# class Worker:
#     def work(self):
#         pass
#     def eat(self):
#         pass
#
# class Manager:
#     def manage(self):
#         pass
#
# class SuperWorker:
#     def work(self):
#         pass
#     def eat(self):
#         pass
#     def manage(self):
#         pass


class WorkerInterface:
    def work(self):
        pass


class EaterInterface:
    def eat(self):
        pass


class ManagerInterface:
    def manage(self):
        pass


class Worker(WorkerInterface, EaterInterface):
    def work(self):
        pass

    def eat(self):
        pass


class Manager(ManagerInterface):
    def manage(self):
        pass


class SuperWorker(WorkerInterface, EaterInterface, ManagerInterface):
    def work(self):
        pass

    def eat(self):
        pass

    def manage(self):
        pass

# 8. Дан код. Исправить его в соответствии с принципом Dependency Inversion.

# class LightBulb:
#     def turn_on(self):
#         print("Лампочка включена")
#
# class Switch:
#     def __init__(self, bulb):
#         self.bulb = bulb
#
#     def operate(self):
#         self.bulb.turn_on()
#
# bulb = LightBulb()
# switch = Switch(bulb)
# switch.operate()

class LightBulb:
    def turn_on(self):
        print("Лампочка включена")


class TV:
    def turn_on(self):
        print("Телевизор включен")


class Switch:
    def __init__(self, notifier):
        self.notifier = notifier

    def operate(self, notifier):
        self.notifier.turn_on()


bulb = LightBulb()
switch = Switch(bulb)
switch.operate(bulb)

tv = TV()
switch = Switch(tv)
switch.operate(tv)
