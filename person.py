import math


age: int = 0

vladimir_age = 38
vladimir_fio = "Vladimir"

oleg_age = 20
oleg_fio = "Oleg"


class Rectangle:
    def __init__(self, x: float, y: float):
        if x <= 0 or y <= 0:
            raise Exception("Не может быть прямогольник со стороной ноль или меньше")
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y

    def square_of_inner_circle(self) -> float:
        radius = min(self.x, self.y) / 2.0
        return math.pi * radius * radius

    def shortest_path_to_edge(self, c_coord, y_coord):
        # вставить алгоритм Яши
        pass


r1 = Rectangle(5.0, 7.0)
print(r1.square())
print(r1.square_of_inner_circle())

r2 = Rectangle(0.0, 7.0)


class Person:

    def __init__(self, age: int, fio: str):
        # Конструктор — метод, который вызывается при конструировании экземпляра (объекта) класса.
        self.age = age
        self.fio = fio

    def is_allowed_to_vote(self) -> bool:
        return self.age >= 18

    @staticmethod
    def is_subject_of_human_rights() -> bool:
        # source: https://www.un.org/ru/documents/decl_conv/declarations/declhr.shtml
        # Все люди рождаются свободными и равными в своем достоинстве и правах. Они наделены разумом и совестью и
        # должны поступать в отношении друг друга в духе братства.
        return True


print(f'Is person is subject of human rights: {Person.is_subject_of_human_rights()}')

# Конструирование (инициализация) первого объекта
vladimir = Person(age=38, fio='Vladimir')

# Конструирование (инициализация) второго объекта
oleg = Person(age=17, fio='Oleg')


print(f'Vladimir\'s age: {vladimir.age} and his voting status: {vladimir.is_allowed_to_vote()} and is subject of human rights: {vladimir.is_subject_of_human_rights()}')
print(f'Oleg\'s age: {oleg.age} and his voting status: {oleg.is_allowed_to_vote()}  and is subject of human rights: {vladimir.is_subject_of_human_rights()}')
