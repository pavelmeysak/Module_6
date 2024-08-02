class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __colour, __engine_power):
        self.owner = str(owner)
        self.model = str(__model)
        self.colour = str(__colour)
        self.engine_power = int(__engine_power)

    def get_model(self):
        print(f'Модель: {self.model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.engine_power}')

    def get_colour(self):
        print(f'Цвет: {self.colour}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_colour()
        print(f'Владелец: {self.owner}')

    def set_colour(self, new_color):
        if self.__COLOR_VARIANTS.__contains__(new_color.lower()):
            self.colour = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_colour('Pink')
vehicle1.set_colour('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
