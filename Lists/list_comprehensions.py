# prev_list = [1, 2, 3]

# new_list = []

# for item in prev_list:
#     new_list.append(item * 2)

# print(new_list)

# new_list = [i*2 for i in prev_list]

# print(new_list)

# language = "Python"

# print([letter for letter in language])

prev_list = [10, -5, 20, 30, -10, -1, 2, 7, 90]

# positive_numbers = [num for num in prev_list if num > 0]

# print(positive_numbers)

# squares = [x**2 for x in prev_list if x < 0]

# print(squares)

""" def is_consonant(char):
    return char.isalpha() and char.lower() not in "aeiou"

sentence = "My name is Elshad"
consonants = [char for char in sentence if is_consonant(char)]

print(consonants) """


def get_number(number):
    return number if number > 0 else 'negative number'


new_list = [
    get_number(num)
    for num in prev_list
]

print(new_list)
