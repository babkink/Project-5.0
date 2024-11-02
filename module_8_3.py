class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = vin
        self.__number = number
        self.__is_valid_vin(self.__vin)
        self.__is_valid_number(self.__number)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f"Incorrect VIN number: {vin_number}")
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(f'Wrong range for VIN number - it should be from 1000000 to 9999999 but '
                                     f'we got {vin_number}')
        else:
            return True

    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers(f'Incorrect type for number: {number} - should be string')
        elif len(str(number)) != 6:
            raise IncorrectCarNumbers(f'Lenght of number should be 6 digits, but we got {number}')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
