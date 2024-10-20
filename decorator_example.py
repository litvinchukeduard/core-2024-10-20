from datetime import datetime
from functools import wraps
'''
Написати декоратор, який буде виводити інформацію про виклик функції
'''

# calculate_sum([1, 2, 3, 4, 5])
# 15:30 2024-10-20
# Calling function "calculate_sum"
# With arguments: "[1, 2, 3, 4, 5]"
# Result is: "15"

def info_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(datetime.now())
        print(f'Calling function "{func.__name__}"')
        print("With arguments:")
        for arg in args:
            print(arg)

        for (key, value) in kwargs.items():
            print(f"{key}={value}")

        # print(args, kwargs)
        result = func(*args, **kwargs)
        print(f'Result is: "{result}"')
        return result

    return wrapper

@info_decorator
def calculate_sum(a, b, numbers_list: list[int]) -> int:
    """ Function that calculates sum of numbers """
    return sum(numbers_list)

@info_decorator
def calculate_sum_alternative(*args, **kwargs):
    sum = 0
    for number in args:
        sum += number
    
    for (key, value) in kwargs.items():
        sum += value
    return sum


# print(datetime.now())
# print(dir(calculate_sum))

# calculate_sum.__name__ = "hello_world"

# print(calculate_sum.__name__)

# calculate_sum(1, 2, numbers_list=[1, 2, 3, 4])

# print(calculate_sum_alternative(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(calculate_sum_alternative(a=1, b=2, c=3, hello=4))

# print(*[1, 2, 3, 4])
# print(1, 2, 3, 4)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(calculate_sum_alternative(**my_dict))

# print(1, 2, 3, 4, 5,)
# sum([1, 2, 3, 4])
# print(calculate_sum.__doc__)

print(calculate_sum.__name__)
print(calculate_sum.__doc__)
