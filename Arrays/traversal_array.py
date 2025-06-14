from array import array


def access_element(arr, index):
    if index >= len(arr) or index < -len(arr):
        return f"index {index} does not exist!"

    return arr[index]


def traverse_array(arr):
    for e in arr:
        print(e)


#                       index
#                       0    1    2    3
#                      -4   -3   -2   -1
char_arr = array('u', ['a', 'b', 'c', 'd'])

traverse_array(char_arr)
print(access_element(char_arr, 4))
