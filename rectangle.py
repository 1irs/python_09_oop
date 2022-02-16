class MyClass:
    pass


m = MyClass()
print(m)


class Rectangle:
    """
    Класс моделирует прямоугольник.
    """
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_ploshad(self) -> float:
        """Подсчитывает площадь прямоугольника"""
        return self.a * self.b

    def is_kvadrat(self) -> bool:
        """Является ли этот прямоугольник квадратом"""
        return self.a == self.b

    def get_perimeter(self) -> float:
        return (self.a + self.b) * 2


r1 = Rectangle(10.0, 20.0)
r2 = Rectangle(30.0, 30.0)

print(str(r1))

r1_ploshad = r1.get_ploshad()
r2_ploshad = r2.get_ploshad()
r1_is_kvadrat = r1.is_kvadrat()
r2_is_kvadrat = r2.is_kvadrat()

print(f"Площадь прямоугольника {r1_ploshad}, он квадрат: {r1_is_kvadrat}")
print(f"Площадь прямоугольника {r2_ploshad}, он квадрат: {r2_is_kvadrat}")
