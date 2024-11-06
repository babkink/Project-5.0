first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_res = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
second_res = (len(first[x]) == len(second[x]) for x in range(len(first)))

print(list(first_res))
print(list(second_res))