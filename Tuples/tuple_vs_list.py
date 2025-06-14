list1 = [0, 1, 2, 3, 4, 5, 6, 7]

list1[1] = 3

print(list1)

list1 = [7, 6, 5, 4, 3, 2, 1]

print(list1)

del list1[0]
del list1[:]

print(list1)

tuple1 = 1, 2, 3, 4, 5, 6, 7
# tuple1[1] = 10

del tuple1

# print(tuple1)

l_tups = [(1, 2), (3, 4), (5, 6)]

print(l_tups)

tup_ls = ([1, 2], (3, 4), [1])

tup_ls[0].append(100)

print(tup_ls)
