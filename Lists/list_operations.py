# a = [1, 2, 3]
# b = [4, 5, 6, 7]

# c = a + b

# print(c)

# a = [0]

# print(a * 4)

# a = [0, 1, 2, 3, 4, 5, 6]

# l = len(a)
# print(l)
# print(max(a))
# print(min(a))
# t = sum(a)
# print(t)
# print(l/t)

# total = count = 0

# while True:
#     inp = input("enter a number: ")

#     if inp == "done":
#         break

#     num = float(inp)

#     total += num
#     count += 1

# avg = total / count
# print(f"average: {avg:.2f}")

nums = []

while True:
    inp = input("enter a number: ")

    if inp == "done":
        break

    num = float(inp)
    nums.append(num)

avg = sum(nums) / len(nums)
print(f"average: {avg:.2f}")
