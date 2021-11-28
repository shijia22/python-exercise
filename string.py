my_string = 'abcdefg'

# slicing
print(my_string[0])
# a
print(my_string[2:])
# cdefg
print(my_string[:2])
# ab
print(my_string[:])
# abcdefg
print(my_string[::])
# abcdefg
print(my_string[::2])
# acef

# upper 大寫
x = my_string.upper()
print(x)

# lower 小寫
y = x.lower()
print(y)

# spilt
z = my_string.split('b')
print(z)
# ['a', 'cdefg']

# print format
a = 'item one: {}; item two: {} '.format('dog', 'cat')
print(a)