from dataclasses import dataclass


def custom_write(file_name, strings):

    n = 1
    for i in strings:
        file = open(file_name, "a", encoding='utf-8')
        a = file.tell()
        file.write(f'{i}\n')
        string_positions[(n, a)] = i
        file.close()
        n += 1
    return string_positions




string_positions = {}
file_name = 'Text 7.2.txt'
# strings = ('I', 'R', 'Я', 'U')
strings = ('I study Python', 'English is foreign language', 'Русский мой родной язык', 'Urban')
res = custom_write(file_name, strings)

for i in res.items():
    print(i)

data = open(file_name, 'r')
n = 1
for j in data:
    print(n, j.strip())
    n += 1
