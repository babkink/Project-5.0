from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(len(first))
print(len(second))
print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name):
    f = open(file_name, 'w')
    def write_everithing(*args):
        for i in args:
            f.writelines(str(i) + '\n')
        f.close()
    return write_everithing

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

f = MysticBall('А', 'это', 'уже', 'число', 5, 'в', 'списке')
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
