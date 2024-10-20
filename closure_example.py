'''
Написати функцію, яка буде генерувати унікальне id
'''

current_id = 0 # 145654546

def get_next_id():
    global current_id
    current_id += 1
    return current_id

def get_next_id_alternative():
    global current_id
    current_id -= 1
    return current_id

def gen_next_id_closure():
    current_id = 0

    def calculate_next_id():
        nonlocal current_id
        current_id += 1
        return current_id
    
    return calculate_next_id

# print(get_next_id())
# print(get_next_id())
# print(get_next_id())
# print(get_next_id())

# print()

# print(get_next_id_alternative())
# print(get_next_id_alternative())
# print(get_next_id_alternative())
# print(get_next_id_alternative())

# print(gen_next_id_closure()())
# print(gen_next_id_closure()())
# print(gen_next_id_closure()())
get_next_unique_id = gen_next_id_closure()
# print(get_next_unique_id)

print(get_next_unique_id())
print(get_next_unique_id())
print(get_next_unique_id())
print(get_next_unique_id())

get_next_unique_id_two = gen_next_id_closure()

print(get_next_unique_id_two())
print(get_next_unique_id_two())
print(get_next_unique_id_two())
print(get_next_unique_id_two())

del get_next_unique_id_two
get_next_unique_id_two = gen_next_id_closure()
print(get_next_unique_id_two())
