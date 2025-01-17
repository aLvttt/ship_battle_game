from core import Field, Ship, Player
'''

# блок типо регестрации
print("Welcome to Battleship! Enter your name: ")
playername = input()
print(f"Hello, {playername}! Let's start the game!")

'''
player_types = ['player', 'bot']
player = Player(player_types[0])
bot = Player(player_types[1])

player_field = Field(player)
bot_field = Field(bot)

print(player_field.owner)
print(bot_field.owner)
#print(Field.__dict__.values())
