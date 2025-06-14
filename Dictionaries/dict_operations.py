my_dict = {
    3: "three",
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four"
}

my_dict1 = {
    0: "zero",
    1: "False"
}


print("ten" not in my_dict.values())
print(len(my_dict))
print(all(my_dict))
print(all(my_dict1))
print(any(my_dict1))

print(sorted(my_dict))
