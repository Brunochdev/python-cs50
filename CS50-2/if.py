# Início de condicionais usando IF e um pouco de OR

x = int(input('Whats the value of "X"? '))
y = int(input('Whats the value of "Y"? '))

if x > y:
    print('X is greater than Y')
elif x < y:
    print('X is less than Y')
else:
    print('X is equal to Y')

if x < y or x > y:
    print('x is not equal to y')
else:
    print('x is equal to y')

if x == y:
    print('X is equal to Y')
else:
    print('X is not equal to Y')

