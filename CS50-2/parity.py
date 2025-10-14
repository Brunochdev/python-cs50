# Operadores aritméticos em módulo

def main():
    x = int(input('Whats the value of X? '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  

main()      

# #Versão 2 do is_even
# def is_even(n):
#   return True if n % 2 == 0 else False #Aqui basicamente vai deixar tudo em uma linha apenas

# #Versão 3 do is_even
# def is_even(n):
#   return n % 2 == 0 #Aqui vai simplesmente assumir que é True caso cumpra a condição