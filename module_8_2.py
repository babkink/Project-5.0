
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Wrong data type in personal_sum: {i}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        int_float_count = len([item for item in numbers if isinstance(item, (int, float))])
        res = personal_sum(numbers)[0] / int_float_count
        return res
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('Wrong data type in calculate_average')
        return None

print(calculate_average((1,2,3,4,'five')))
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


