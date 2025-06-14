from typing import Any


def linear_search(p_list: list, p_target: Any) -> int:
    for i, value in enumerate(p_list):
        if value == p_target:
            return i

    return -1


my_list = [x*10 for x in range(8)]

target = 50

# if target in my_list:
#     print(f"{target} is in the list")
# else:
#     print(f"{target} is not in the list")

print(linear_search(my_list, target))
