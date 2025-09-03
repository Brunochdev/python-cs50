# Aqui começa o curso do CS50P

##print('Bruno, this is your first "hello, world!"')

# Agora vem a evolução

name = input('''Qual o seu nome? 
Resposta: ''') #esse input fará com que pergunte e a variável seja definida com o valor passado e as três aspas são pra manter a estrutura do texto
# print(name, end="") #Esse sinal de "end=" faz com que o que era antes default \n não aconteça, mas sim continue sem parar as linhas
# print(', this is your second "hello, world!"')
# #Bruno, this is your second "hello, world!"
# print('This line is separated by a diferent value', name, sep="***")#Esse sinal de "sep=" faz com que mude o valor nos espaços
# #This line is separated by a diferent value***Bruno

# E finalmente, o melhor modo, o mais utilizado hoje em dia.

print(f'{name}, this is your third "hello, world!"', )#Finalmente fazendo a chamada em uma linha apenas. Fica melhor visualmente


# NOTES: 
### GUI = Graphical User Interface. É a interface gráfica do usuário
### Documentação Python: docs.python.org