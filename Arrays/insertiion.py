import array

my_arr = array.array('i', [1, 2, 3, 4])

print(my_arr)

my_arr.insert(0, 6)

print(my_arr)

my_arr.insert(2, 10)

print(my_arr)

my_arr.insert(100, 100)

print(my_arr)
