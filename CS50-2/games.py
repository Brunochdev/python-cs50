# Entendendo o match

game = input('Whats the name of the game: ')

# # A estrutura a seguir funciona, mas existe uma outra abordagem
# if game == 'Pokemon':
#     print('This game is from GameBoy')
# elif game == 'Chrono Trigger':
#     print('This game is from Snes')
# elif game == 'Final Fantasy 6':
#     print('This game is from Snes')
# elif game == 'Super Mario World':
#     print('This game is from Snes')
# else:
#     print("I don't know where this game is from")

match game:
    case 'Pokemon':
        print('This game is from GameBoy')
    case 'Chrono Trigger' | 'Final Fantasy 6' | 'Super Mario World':
        print('This game is from Snes')   
    case _: #Esse "_" serve para dizer "qualquer valor"
        print("I don't know where this game is from") 