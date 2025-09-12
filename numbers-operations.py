# Novo arquivo para tratar números

#Int, Float, round and operations
x = int(input("Whats the value of x? "))
y = float(input("Whats the value of y? "))

z = round(x + y) # Apenas um retorno de uma soma arredondada 
zdiv = round(x / y, 4) # Aqui ele arredonda a divisão e retorna com 4 casas após o ponto
sum = z + zdiv 

print(f'The final value is: {x + y}')
print(f'Using "round" the value is: {z:,}') # Aqui seria algo para a casa do milhar, ia dividir com vírgula
print(f'The division "rounded" is: {zdiv}') 
print(f'And finally the sum rounded is: {sum:.2f}') # Esse 2f indica que é pra retornar duas casas após o ponto

#Esse vai ser o resultado final de tudo:
# Whats the value of x? 5
# Whats the value of y? 5.7
# The final value is: 10.7
# Using "round" the value is: 11
# The division "rounded" is: 0.8772
# And finally the sum rounded is: 11.88