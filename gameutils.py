from hero import *
from villain import *
from weapon import *
from utils import *
import random
import math

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
¡Salva al pueblo de las amenazas!

Pulsa intro tecla para continuar...
''')
    input()

def chooseHero():
	x = 0
	while x not in [1, 2]:
		cls()
		print('''
¡Escoge Heroe y arma y lucha por el honor!

1. Guerrero
2. Arquero

''')
		x = readInt('Selecciona un héroe: ', 'Illo, un numero, joder')

	return x

def createWarrior():
	name = input("¿Cómo se llama tu Guerrero?: ")
	return Warrior(name)

def createArcher():
	name = input("¿Cómo se llama tu Arquero?: ")
	return Archer(name)


def chooseWeapon(hero):
	print(type(hero))
	if isinstance(hero, Warrior):
		x = 0
		while x not in [1, 2]:
			cls()
			print('''
¡Bien, Guerrero %s! Escoge tu arma

1. Espada Inicial (10P)
2. Maza Española  (14P)

''' % hero.name)
			x = readInt('Selecciona un arma: ', 'Illo, un numero, joder')
		if x == 1:
			return Sword("Inicial", 10, 14)
		elif x == 2:
			return Mace("Española", 14, 19)

	elif isinstance(hero, Archer):
		x = 0
		while x not in [1, 2]:
			cls()
			print('''
¡Bien, Arquero %s! Escoge tu arma

1. Arco Boli (7P)
2. Ballesta Tirachina  (11P)

''' % hero.name)
			x = readInt('Selecciona un arma: ', 'Illo, un numero, joder')
		if x == 1:
			return Bow("Boli", 7, 9)
		elif x == 2:
			return Crossbow("Tirachina", 11, 14)
	else:
		print("\nNo sé por qué estoy aqui\n\n")

	

def createWarrior():
	name = input("¿Cómo se llama tu Guerrero?: ")
	return Warrior(name)

def createArcher():
	name = input("¿Cómo se llama tu Arquero?: ")
	return Archer(name)

def combat(hero, villain):
	if random.randint(1,20) <= 16:
		turno = 1
		print("Empieza el héroe")
	else:
		turno = 2
		print("Ataca el enemigo!")

	fighting = True
	while fighting:
		if turno == 1:
			opcion = 0
			while opcion not in [1, 2, 3]:
				cls()
				print(hero)
				print('''
Te enfrentas a %s, ¿Qué quieres hacer?
1. Atacar
2. Defender
3. Sanar				
					''' % villain.name)
				opcion = readInt('Selecciona una opcion: ', 'Illo, un numero, joder')
			if opcion == 1:
				res = attack(hero, villain)
				
				if res['status'] == 0:
					print(f"Fallas y no causas daño a {villain.name}")	
				elif res['status'] == 1:
					print(f"Causas {res['damage']} puntos de daño a {villain.name}")
				elif res['status'] == 2:
					print(f"Causas {res['damage']} puntos de daño a {villain.name}")
					print(f"Has derrotado a {villain.name}!!")
					fighting = False
					victory = True
				
			elif opcion == 2:
				hero.defending(1)
				print("Te preparas para defender")
			elif opcion == 3:
				heal_val = math.ceil(25 + hero.stats['dex'] * 0.8)
				hero.heal(heal_val)
				print(f"Te curas {heal_val} puntos de vida")
			turno = 2
			input("Pulsa una tecla para continuar...")
			




		elif turno == 2:
			input(f"\n\nTurno del enemigo {villain.type} {villain.name}")

			health_per = villain.stats['health'] / villain.stats['health_max'] * 100
			
			dice = random.randint(1,20)

			if health_per < 20:
				
				if  dice >= 12:

					heal_val = math.ceil(villain.stats['health_max'] * 0.25)
					villain.heal(heal_val)
					print(f"{villain.name} se cura {heal_val} puntos de vida")

				elif dice >= 8:

					villain.defending(1)
					print(f"{villain.name} se prepara para defender")

				else:

					res = attack(villain, hero)
					if res['status'] == 0:
						print(f"{villain.name} falla y no te causa daños")	
					elif res['status'] == 1:
						print(f"{villain.name} te causa {res['damage']} puntos de daño")
					elif res['status'] == 2:
						print(f"{villain.name} te ha matado :(")
						fighting = False
						victory = False

			elif health_per < 80:
				
				if  dice >= 19:
					
					heal_val = math.ceil(villain.stats['health_max'] * 0.2)
					villain.heal(heal_val)
					print(f"{villain.name} se cura {heal_val} puntos de vida")

				elif dice >= 15:

					villain.defending(1)
					print(f"{villain.name} se prepara para defender")

				else:
					res = attack(villain, hero)

					if res['status'] == 0:
						print(f"{villain.name} falla y no te causa daños")	
					elif res['status'] == 1:
						print(f"{villain.name} te causa {res['damage']} puntos de daño")
					elif res['status'] == 2:
						print(f"{villain.name} te ha matado :(")
						fighting = False
						victory = False

			else:

				if  dice >= 18:
					villain.defending(1)
					print(f"{villain.name} se prepara para defender")
				else:
					res = attack(villain, hero)
					if res['status'] == 0:
						print(f"{villain.name} falla y no te causa daños")	
					elif res['status'] == 1:
						print(f"{villain.name} te causa {res['damage']} puntos de daño")
					elif res['status'] == 2:
						print(f"{villain.name} te ha matado :(")
						fighting = False
						victory = False
			
			turno = 1
			input("Pulsa una tecla para continuar...")



	return victory

def attack(attacker, enemy):
	dice_attacker = random.randint(1,20)
	dice_enemy = random.randint(1,15)
	print("""
---------
¡Destrezas!
Atacante: %s + %s
Atacado: %s + %s
""" % (dice_attacker, attacker.stats['dex'], dice_enemy, enemy.stats['dex']))

	if dice_attacker == 20:
		
		
		weapon_damage = attacker.weapon.attack() if attacker.weapon != None else 0
		attacker_damage = round(attacker.stats[attacker.main_attr_attack] * 0.8)
		damage_reduction = round(enemy.stats['defense'] * (0.5 + enemy.defending_flag * 0.5))
		total_damage = weapon_damage + attacker_damage - damage_reduction if damage_reduction < weapon_damage + attacker_damage else 1

		alive = enemy.damage(total_damage)

		enemy.defending(0)

		if alive:
			return {"status" : 1, "damage" : total_damage, "weapon_damage" : weapon_damage, "attacker_damage" : attacker_damage, "damage_reduction" : damage_reduction}
		else:
			return {"status" : 2, "damage" : total_damage, "weapon_damage" : weapon_damage, "attacker_damage" : attacker_damage, "damage_reduction" : damage_reduction}


	elif dice_attacker + attacker.stats['dex'] >= dice_enemy + enemy.stats['dex']:
		
		weapon_damage = attacker.weapon.attack() if attacker.weapon != None else 0
		attacker_damage = round(attacker.stats[attacker.main_attr_attack] * 0.2)
		damage_reduction = round(enemy.stats['defense'] * (0.7 + enemy.defending_flag * 0.7))
		total_damage = weapon_damage + attacker_damage - damage_reduction if damage_reduction < weapon_damage + attacker_damage else 1

		alive = enemy.damage(total_damage)

		enemy.defending(0)

		if alive:
			return {"status" : 1, "damage" : total_damage, "weapon_damage" : weapon_damage, "attacker_damage" : attacker_damage, "damage_reduction" : damage_reduction}
		else:
			return {"status" : 2, "damage" : total_damage, "weapon_damage" : weapon_damage, "attacker_damage" : attacker_damage, "damage_reduction" : damage_reduction}


	else:
		return {"status" : 0, "damage" : 0}
	
