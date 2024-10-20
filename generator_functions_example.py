'''
Написати функцію-генератор, яка симулює кидання 8 кубиків і за раз повертати лише один
'''

import random

# random.randint()

# print(random.randint(1, 6))

# results = []
# for i in range(8):
#     results.append(random.randint(1, 6))
# print(results)

# print([random.randint(1, 6) for i in range(8)])

def generate_random_dice_rolls(n: int):
    result = [random.randint(1, 6) for _ in range(n)]
    for value in result:
        yield value

def generate_random_dice_rolls_inplace(n: int):
    for _ in range(n):
        yield random.randint(1, 6)

'''Написати функцію, яка буде повертати по рядку з файлу'''
def get_file_lines(path: str):
    with open(path, 'r') as file:
        for line in file:
            yield line

# dice_rolls_generator = generate_random_dice_rolls(8)
# print(dice_rolls_generator)
# print(next(dice_rolls_generator))
# print(next(dice_rolls_generator))

# dice_rolls_generator = generate_random_dice_rolls_inplace(8)
# print(next(dice_rolls_generator))
# print(next(dice_rolls_generator))
# print(next(dice_rolls_generator))

# my_generator = get_file_lines('list_comprehensions_example.py')
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

# random_generator = (random.randint(1, 6) for _ in range(5))
# print((random.randint(1, 6) for _ in range(8)))
# print(next(random_generator))
# print(next(random_generator))
# print(next(random_generator))
# print(next(random_generator))
# print(next(random_generator))
# print(next(random_generator))

dice_rolls_generator = generate_random_dice_rolls(8)
print([*dice_rolls_generator])
