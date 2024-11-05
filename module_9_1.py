from unittest import removeResult


def min_(list):
    return min(list)

def max_(list):
    return max(list)

def len_(list):
    return len(list)

def sum_(list):
    return sum(list)

def sorted_(list):
    return sorted(list)

def multiply_by_two(list_):
    return list(map(lambda x: x * 2, list_))

def squ(n):
    return n ** 2

def square(list_):
    return list(map(squ, list_))

def apply_all_func(list, *args):
    result = {}
    for func in args:
        result[func.__name__] = [func(list)]
    return result

a = [5,4,3,2,1]
print(apply_all_func(a, square, min_, max_, len_,sum_, sorted_, multiply_by_two))