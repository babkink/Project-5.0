from operator import ifloordiv

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = list(dict([(x, len(x))]) for x in first_strings + second_strings if len(x) % 2 == 0)
# не получилось записать третий результат в один словарь - каждая пара получилась в новом словаре. Подскажите, что делал не так?

print(first_result)
print(second_result)
print(third_result)
