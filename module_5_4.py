class House:
    house_history = []
    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но остается в истории')
        del self

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors:
            print(f'"Такого этажа не существует",{self.name}')
        else:
            for i in range(1, self.new_floor + 1):
                print(i, self.name)
    def build(self):
        self.number_of_floors = self.number_of_floors + 1
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, int):
            return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h2 = House('ЖК Акация', 20)
print(House.house_history)
h3 = House('Ромашка', 22)
print(House.house_history)
h4 = House('Town at the coast', 3)

print(h1)
print(h2)
print(h3)
print(h4)
print(House.house_history)
del h1
print(House.house_history)
del h2
print(House.house_history)
