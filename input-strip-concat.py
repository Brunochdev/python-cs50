# Aqui começa o curso do CS50P

name = input('''Qual o seu nome? 
Resposta: ''')
# name = input('''Qual o seu nome? 
# Resposta: ''').strip().title()

sobreNome = input('''Qual o seu sobrenome? 
Resposta: ''')

sobreNome = sobreNome.capitalize()
name = name.strip().title()

print(f'{name} {sobreNome}, this is something way better!!')


# NOTES: 
### GUI = Graphical User Interface. É a interface gráfica do usuário
### Documentação Python: docs.python.org
### python -i .\python-sprint1.py exemplo de como rodar o python em modo interativo
