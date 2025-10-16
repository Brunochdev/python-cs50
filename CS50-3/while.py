# Iniciando com loops while

itsOk = 0
count = 5


def number_ok():
    x = int(input('Whats the initial value of x? '))    
    while x <= 10:
        print('Agora o valor de x é: ', x)
        x += 1
number_ok()

while itsOk < 3:
    print('Ok')
    itsOk += 1

while itsOk <= 5:
    print(f'Ok', itsOk)
    itsOk += 1

while count != 0:
    print(count)
    count -= 1

#Os resultados serão esses
# Ok
# Ok
# Ok
# Ok {3} Observe que aqui apesar de o "itsOk" começar em 0, nessa parte vai começar em 3 pq o laço já foi percorrido anteriormente até 3 no primeiro while
# Ok {4}
# Ok {5} 
# 5
# 4
# 3
# 2
# 1

