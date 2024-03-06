import random

class robot:
	def __init__ (self, name, atk, hp):
		self.name = name
		self.atk = atk
		self.hp = hp

	def battle(attack_input):
		enemy_input = random.randint(1, 3)
		print("")
		if attack_input == 1:
			print("Player choose Power!")
		elif attack_input == 2:
			print("Player choose Technique!")
		elif attack_input == 3:
			print("Player choose Speed!")

		if enemy_input == 1:
			print("Enemy choose Power!")
		elif enemy_input == 2:
			print("Enemy choose Technique!")
		elif enemy_input == 3:
			print("Enemy choose Speed!")
			
		if attack_input == enemy_input:
				print("It's a draw! Both robots take no damage.")
		elif (attack_input == 1 and enemy_input == 2) or (attack_input == 2 and enemy_input == 3) or (attack_input == 3 and enemy_input == 1):
				print("Player robot wins! Enemy robot takes damage.")
				icarus.hp -= daedalus.atk
		else:
				print("Enemy robot wins! Player robot takes damage.")
				daedalus.hp -= icarus.atk
		print("")

icarus = robot("Icarus", 10, 100)
daedalus = robot("Daedalus", 10, 100)

print("Robot fighting game (Power, Technique, Speed)!")
print("Power beats Speed, Technique beats Power, Speed beats Technique.")
while daedalus.hp != 0 and icarus.hp != 0:
	print(f"Player HP : {icarus.hp}, Attack point : {icarus.atk}")
	print(f"Enemy HP : {daedalus.hp}, Attack point : {daedalus.atk}")
	print("Choose attack type: ")
	print("[1] Power, [2] Technique, [3] Speed, [4] Quit")
	attack_input = int(input())
	if attack_input > 0 and attack_input <= 3:
		robot.battle(attack_input)
	elif attack_input == 4:
		icarus.hp = 0
	else:
		print("Invalid input. Please choose again.")

if daedalus.hp == 0:
    print("Player wins!")
elif icarus.hp == 0:
    print("Enemy wins!")
