
def is_prime(func):
    def wrapper(*args):
        var = func(*args)
        for i in range(2, var - 1):
            if var % i == 0:
                return f'Not prime\n{func(*args)}'
        return f'Prime\n{func(*args)}'
    return wrapper


@is_prime
def sum_three(*nums):
    return sum(nums)

result = sum_three(1,2,3,5)
print(result)

