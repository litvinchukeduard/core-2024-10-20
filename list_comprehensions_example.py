'''
В нас є список з слів, потрібно написати функцію, яка буде скорочувати ці слова до певного розміру і додавати в кінці ...
'''

# 3
WORD_LIST = [
    "Supercalifragilisticexpialidocious", # "Sup...""
    "Incomprehensibilities", # "Inc..."
    "Honorificabilitudinitatibus" # "Hon..."
]

# 6
def shorten_words(words_list: list[str], length: int) -> list[str]:
    if length <= 3:
        raise ValueError("Length can not be less than 3")
    result_list = []
    for word in words_list:
        # if len(word) > 3:
            new_word = f"{word[:length - 3]}..."
            result_list.append(new_word)
    return result_list

def shorten_words_alternative(words_list: list[str], length: int) -> list[str]:
    if length <= 3:
        raise ValueError("Length can not be less than 3")
    # return [f"{word[:length - 3]}..." for word in words_list if len(word) > 3]
    return [f"{word[:length - 3]}..." for word in words_list]

# 10 => 10 - 2 = 8
# print("Supercalifragilisticexpialidocious"[:-33])


print(shorten_words_alternative(WORD_LIST, 4))
print(WORD_LIST)
