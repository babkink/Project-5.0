from calendar import firstweekday
from tkinter.constants import SEL_FIRST


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    def get_model(self):
        return f'Vehicle model is {self._model}'

    def get_horsepower(self):
        return f'Vehicle horsepower is {self._engine_power}'

    def get_color(self):
        return f'Vehicle color is {self._color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nOwner is {self.owner}')

    def set_color(self, new_color):
        if any(i == new_color.lower() for i in self.__COLOR_VARIANTS):
            self._color = new_color
        else:
            print(f'It is impossible to change color to {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def get_pass_limit(self):
        return print(f'Passengers limit is {self.__PASSENGERS_LIMIT}')

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedor', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
print()
vehicle1.get_pass_limit()