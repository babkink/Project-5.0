from sys import modules


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors:
            print(f'"Такого этажа не существует",{self.name}')
        else:
            for i in range(1, self.new_floor + 1):
                print(i, self.name)
                

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Golden field', 12)
h1.go_to(5)
h2.go_to(10)
h3.go_to(10)