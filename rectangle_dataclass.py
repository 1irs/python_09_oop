from dataclasses import dataclass


@dataclass
class Rectangle:
    """
    Класс моделирует прямоугольник.
    """

    a: float
    b: float
    color: str = "black"

    def get_ploshad(self) -> float:
        return self.a * self.b

    def is_kvadrat(self) -> bool:
        return self.a == self.b


r1 = Rectangle(a=10.0, b=20.0, color='red')
r2 = Rectangle(a=30.0, b=30.0)

print(f"Площадь прямоугольника {r1.get_ploshad()}, он квадрат: {r1.is_kvadrat()}, его цвет {r1.color}")
print(f"Площадь прямоугольника {r2.get_ploshad()}, он квадрат: {r2.is_kvadrat()}, его цвет {r2.color}")
