a = "spam spam spam"
b = list(a)
c = a.split()
print(b)
print(c)

s = "spam-spam1-spam2"
delimiter = '-'
print(s.split(delimiter))

print(s.split('a'))

print('-'.join(s.split('-')))
