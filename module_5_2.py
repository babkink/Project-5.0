class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Golden field', 12)
h1.go_to(5)
h2.go_to(10)
h3.go_to(10)
print()
print(str(h1))
print(str(h2))
print(str(h3))
print()
print(len(h1))
print(len(h2))
print(len(h3))