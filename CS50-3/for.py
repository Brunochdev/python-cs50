# Partindo para o aprendizado do FOR

for i in range(4): #lembrando que o i é apenas para declarar e não ficar vazio, pode ser qualquer valor
    print(i+1)

# Uma outra maneira poderia ser
print('Ok\n' * 3, end='') #faz um lopp 3 vezes pulando uma linha e o "end" no final é para não pular a última linha quando terminar     

# Aprofundando

while True:
    n = int(input('Whats the value of x? '))
    if n > 0:
        break

for i in range(n):
    print ('ok', i+1)



def main():
    number = get_number()
    ok(number)

def get_number():
    while True:
        n = int(input('Whats the n value? '))
        if n > 0:
            return n

def ok(n):
    for i in range(n):
        print('Ok', n+1)
        n +=1
main()