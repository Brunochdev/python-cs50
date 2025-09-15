# Início de entendimento de funções

# def for defing

# # aqui eu defino uma função que sempre vai retornar "Hello," e após isso um argumento com valor para "to"
# def hello(to='world'): # essa passagem de valor "world" só que dizer que caso eu chame a função sem passar argumento, ele vai retornar "Hello, world"
#     print('Hello,',to)


# hello() #nesse caso aqui mesmo ele vai retornar "Hello, world" antes mesmo de perguntar "Whats your name"


# # a variável "name" recebe como argumento o valor informado pelo usuário
# name = input('Whats your name? ')
# # então a função é chamada, e o parâmetro "to" recebe o valor "name" pq eu defini isso, caso eu tivesse idade por exemplo eu podia passar como segundo valor
# hello(name)


# estruturando do jeito que tem que ser feito
def main():
    name = input('Whats your name? ')
    hello(name)

def hello(to='world'):
    print('Hello, ', to)

main()


def number():
    x = int(input('Whats the value of x? '))
    print('x squared is:', square(x))

def square(n):
    return pow(n, 2)     

number()