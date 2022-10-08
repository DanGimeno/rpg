from hero import *
from villain import *
from weapon import *
from utils import *
from gameutils import *


cls()

showInstructions()
x = chooseHero()

if x == 1:
	#Warrior
	player1 = createWarrior()
elif x == 2:
	#Arquero
	player1 = createArcher()


#player1 = Warrior("Dan")
#w = Sword("Inicial", 10, 15)
#
#player1.speak()
#player1.show_stats()

w = chooseWeapon(player1)
player1.giveWeapon(w)
player1.showStats()
	

enemy1 = Limo("Limonita")

input(f"\n{player1.name} vs el Limo {enemy1.name}")

resultado = combat(player1, enemy1)

if resultado:
	print("VICTORIA JODER!!")
else:
	print("Derrota...")

input("Pulsa una tecla para continuar")