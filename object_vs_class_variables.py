class SomeClass:

    # Переменная в классе.
    class_variable = 0

    def __init__(self, param1, param2):

        # Переменная в объекте. Свое значение у разных объектов.
        self.param1 = param1

        # Переменная в классе. Одно значение на всех.
        SomeClass.class_variable = param2

    def get_sum(self):
        return self.param1 + SomeClass.class_variable


o1 = SomeClass(10, 20)
print(o1.get_sum())  # Печатает 30
o2 = SomeClass(9, 99)
print(o2.get_sum())  # Печатает 108
print(o1.get_sum())  # Ожидаем 30, а получим 109, т. к. class_variable одна на все объекты
