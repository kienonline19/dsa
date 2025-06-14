from array import array

days = int(input("How many day's temperature? "))

""" temps = []

for i in range(days):
    temps.append(
        float(input(f"Day {i+1}'s high temperature: "))
    )

if days != 0:
    average_temp = sum(temps) / days
    print(f"\nAverage: {average_temp}")

    count = 0

    for temp in temps:
        if temp > average_temp:
            count += 1

    print(f"{count} day(s) above average")
else:
    print("No result!") """

total = 0
temps = array('f')

for i in range(1, days + 1):
    next_temp = float(input(f"Day {i}'s high temp: "))
    total += next_temp
    temps.append(
        next_temp
    )

average = total / days

count = len([temp for temp in temps if temp > average])

print(f"\nAverage: {average:.2f}")
print(f"{count} day(s) above average")
