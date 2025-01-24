from core import Field, Ship, Player


print("Welcome to Battleship! Enter your name: ")

player_types = ['player', 'bot']
player = Player(player_types[0], input(), 2)
bot = Player(player_types[1], 'bot', 2)

player_field = Field(player)
bot_field = Field(bot)

single_celled_ship = Ship(1, 0, 0, '')
double_celled_ship = Ship(2, 0, 0, '')


# блок типо регистрации
print(f"Hello, {player.name}! Let's arrange your ships!")
print(f"You have {player.ships} ships...")
player_field.display()

while player.ships > 0:
    choosen = ''
    print('Choose the ship (enter quantity of ship cells):')
    choosen = input()
    
    if choosen == '1':
        print('Enter coords (x, then y) and direction for ship:')
        single_celled_ship.cord_x = int(input())
        single_celled_ship.cord_y = int(input())
        single_celled_ship.dir = input()

    elif choosen == '2':
        double_celled_ship.cord_x = int(input())
        double_celled_ship.cord_y = int(input())
        double_celled_ship.dir = input()
    else:
        print('You enter incorrect ship. Please, write "1" or "2"...')








'''
print(player.name)
player_field.display()
print('-------')
print(bot.name)
bot_field.display()
'''