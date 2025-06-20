##b1
a = int(input())
b = int(input())
print(a + b - 100)
##b2
n = int(input())
if n % 10 == 0:
    print(n * 17 // 10)
elif n % 10 != 0 and n >= 11:
    print(n * 17 // 10 + n % 10 * 9 // 5 )
else:
    print(n * 9 // 5 + n % 5 * 2)

##b3
n = int(input())
h = 6
c = 0
while n > 0:
    n -= h
    h += 3
    c += 1
print(c)
##b4
n = int(input())
h1 = m1 = h2 = m2 = 0
c = 0
for i in range(1, n + 1):
    if m1 < m2 < h1 < h2:
        c += 1
    h2 += 1
    if h2 == 10:
        h2 = 0
        h1 += 1
    if h1 == 6:
        h1 = 0
        m2 += 1
    if m2 == 10:
        m1 += 1

print(c)
##b5
n = int(input())
s = input()

##b3
n = int(input())
h = 6
c = 0
while n > 0:
    n -= h
    h += 3
    c += 1
print(c)
##b4
n = int(input())
h1 = m1 = h2 = m2 = 0
c = 0
for i in range(1, n + 1):
    if m1 < m2 < h1 < h2:
        c += 1
    h2 += 1
    if h2 == 10:
        h2 = 0
        h1 += 1
    if h1 == 6:
        h1 = 0
        m2 += 1
    if m2 == 10:
        m1 += 1

print(c)
##b5
n = int(input())
s = input()

