
def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        result = str(a) + str(b)
        return result


print(add_everything_up(2,3))
print(add_everything_up(2, 'cow'))
print(add_everything_up('three', 45))
print(add_everything_up('deep', 'three'))