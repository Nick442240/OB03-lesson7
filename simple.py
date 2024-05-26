class MyClass:
    def __init__(self, value):
        self.value = value  # Атрибут экземпляра класса

    def show_value(self):
        print(self.value)  # Доступ к атрибуту экземпляра через self

# Создание конкретных экземпляров класса
obj1 = MyClass(10)  # Конкретный экземпляр 1
obj2 = MyClass(20)  # Конкретный экземпляр 2

# Вызов метода для каждого экземпляра
obj1.show_value()  # Выведет 10
obj2.show_value()  # Выведет 20
