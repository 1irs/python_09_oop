# Смоделировать подсчет веса различных автомобилей.

# Базовый родительский класс автомобилей
# У него нет родительского класса, т. к. это корень.
class Vehicle:

    def __init__(self, ves_kuzova: float):
        """
        Метод-конструктор, который задаст начальное значение
        полей данных (атрибутов).

        Общие атрибуты:
        - руль — не влияет на вес автомобиля
        - колеса — не влияет на вес автомобиля
        - грузоподъемность — влияет!!!
        - цвет — не влияет на вес автомобиля
        - расход топлива на 100 км — не влияет
        - предельная скорость - не влияет
        - тип кузова
        — кол-во пассажиров?

        Влияют на подсчет веса:
        — грузоподъемность
        — загрузка кузова
        — кол-во пассажиров (учитывая средний вес)
        """
        # Вес кузова — единственный атрибут, общий для всех видов автомобилей.
        # Не может быть автомобиля, у которого нет кузова.
        self.ves_kuzova = ves_kuzova

    def get_total_weight(self) -> float:
        """
        Метод подсчитывает полный вес машины, который в себя включает:
        вес кузова + вес полезной нагрузки
        :return:
        """
        # self.ves_kuzova — поле данных (или атрибут) объекта
        # self.get_poleznaya_nagruzka() — метод объекта
        return self.ves_kuzova + self.get_poleznaya_nagruzka()

    def get_poleznaya_nagruzka(self) -> float:
        """
        Метод, который расчитает вес полезной нагрузки.
        :return:
        """
        return 0.0


# Сделаем класс пассажирского автомобиля — он наследуется от Vehicle
class Car(Vehicle):

    def __init__(self, ves_kuzova: float, passenger_count: int):
        """
        Способы конструирования у дочерних классов могут отличаться от родительского.

        passenger_count — количество пассажиров в конкретном автомобиле
        """
        # Родительские классы иногда называют супер-классом.
        # Инициализируем родительский класс.

        # Проверка на количество пассажиров
        if passenger_count > 5:
            print('Нельзя создавать объекты типа Car с количеством пассажиров > 5')

        assert passenger_count <= 5

        super().__init__(ves_kuzova=ves_kuzova)
        self.passenger_count = passenger_count

    def get_poleznaya_nagruzka(self) -> float:
        """
        В легковом автомобиле полезная нагрузка вычисляется по другому алгоритму.
        Поэтому мы не можем оставить родительский метод Vehicle get_poleznaya_nagruzka()
        :return:
        """
        # В формуле расчета полезной нагрузки пассажирского автомобиля
        # мы предпологаем, что средний вес пассажира == 80 кг.
        # А полезная нагрузка пасс. автомобиля считается как кол-во пассажиров * средений вес
        return self.passenger_count * 80.0


# Реализуем класс Truck (Грузовик), он наследуется от Vehicle
class Truck(Vehicle):

    def __init__(self, ves_kuzova: float, gruzopod: float, zagruzka: float):
        """
        Класс Грузовик инициализируется следующими полями:
        1. Вес кузова — т. к. все машины имеют вес кузова.
        2. gruzopod — это общая грузоподъемность грузовика в кг.
        3. zagruzka — на сколько процентов он загружен (от 0.0 до 1.0)
        :param ves_kuzova:
        :param gruzopod:
        :param zagruzka:
        """
        super().__init__(ves_kuzova=ves_kuzova)
        self.gruzopod = gruzopod
        self.zagruzka = zagruzka

    def get_poleznaya_nagruzka(self) -> float:
        """
        В грузовике полезная нагрузка вычисляется по другому алгоритму.
        Поэтому мы не можем оставить родительский метод Vehicle get_poleznaya_nagruzka()
        :return:
        """
        # В формуле расчета полезной нагрузки грузовика
        # мы предпологаем, что полезная нагрузка грузовика
        # считается как максимальная загрузка (gruzopod) * процент загрузки (zagruzka)
        return self.gruzopod * self.zagruzka


car1 = Car(ves_kuzova=1500.0, passenger_count=5)

gruzovik1 = Truck(ves_kuzova=7500.0, gruzopod=10000.0, zagruzka=0.5)

print(f"Полная масса car1 == {car1.get_total_weight()} кг.")
print(f"Полная масса gruzovik1 == {gruzovik1.get_total_weight()} кг.")

spisok_mashin: list[Vehicle] = [car1, gruzovik1]

sum_weight: float = 0.0
for vehicle in spisok_mashin:
    sum_weight = sum_weight + vehicle.get_total_weight()

print(f"Общий вес автомобилей: {sum_weight} кг.")

pass
