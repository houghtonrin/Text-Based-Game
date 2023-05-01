#I Just Need to do try/except and end after 5 days 
#Also fix bugs when they arise
import random
import game
import pickle
class Game():
	def bedroom(inventory):
		Game.save()
		Game.load()
		DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
		DayDescription = ["Time to start the week!", "Productive train! Next stop: YOU", "Hump Day! Let's make the most of it", "You can make it! I believe in you!", "Make sure that you wrap up your work week!"]
		if inventory[1]==True:
			inventory[1] = False
			print(f"\nGood Morning! It is {DAY[inventory[4]]}. {DayDescription[inventory[4]]}")
			inventory[4] += 1
			print(f"You have {inventory[0]} Executive Function Points.")
			BedChoice = input(f"\nWould you like to:\nget out of bed (o): -1 EF point\nor nap (n): +1 to 4 EF points\n")
			if BedChoice == "o":
				inventory[0] -= 1
				RoomChoice = input(f"Would you like to go to the Living Room (l)\nor the Study (st)\n")
				if RoomChoice == "l":
					Game.livingroom(inventory)
					return inventory
				elif RoomChoice == "st":
					Game.study(inventory)
					return inventory
			elif BedChoice =="n":
				hours = random.randint(1,4)
				print("napping...\n"*hours)
				inventory[0] += hours
				print(f"Executive Function Points: {inventory[0]}")
				RoomChoice = input(f"Would you like to go to the Living Room (l)\nor the Study (st)\n")
				if RoomChoice == "l":
					Game.livingroom(inventory)
					return inventory
				elif RoomChoice == "st":
					Game.study(inventory)
					return inventory
		elif inventory[1]==False:
			BedChoice = input(f"\nWelcome to the Bedroom! You see a bed, in a room! Would you like to:\nleave (l)\nnap: +1 to 4 EF Points (n)\nor sleep: start new day (s)\n")
			if BedChoice == "l":
				RoomChoice = input("\nWhat Room do you want to go to?\nLiving Room (l)\nStudy (st)\n")
				if RoomChoice == "l":
					Game.livingroom(inventory)
				if RoomChoice == "st":
					Game.study(inventory)
			elif BedChoice == "n":
				hours = random.randint(1,4)
				print("napping...\n"*hours)
				inventory[0] += hours
				RoomChoice = input("\nWhat Room do you want to go to?\nLiving Room (lr)\nStudy (st)\n")
				if RoomChoice == "lr":
					Game.livingroom(inventory)
				if RoomChoice == "st":
					Game.study(inventory)
			elif BedChoice == "s":
				if inventory[4] > 4:
					print(f"Thank you for playing!")
					quit()
				inventory[1] = True
			Game.bedroom(inventory)
	def study(inventory):
		Game.save()
		Game.load()
		studychoice1 = input(f"\nWelcome to the Study!\nYou see a computer on a desk with a chair.\nWould you like to use it (u)\nor leave (l)\n")
		if studychoice1 == "u":
			studychoice2 = input(f"Would you like to work with high effort: +1 to 5 Job Performance , -3 EF Points (h)\nWork with medium effort: +1 to 3 Job Performance, -2 EF Points (m)\nor Work with Low Effort: +1 Job Performance, -1 EF Point (l)\nIf you would like to leave type l\n")
			if studychoice2 == "h":
				jp = random.randint(1,5)
				inventory[2] += jp
				inventory[0] -= 3
				print(f"You worked with high effort!\nYour Job Performace is {inventory[2]} and your Executive Function points are at {inventory[0]}\n")
				RoomChoice = input(f"What room do you want to go to?\nthe Kitchen (k)\nor the Bedroom (b)\n")
				if RoomChoice == "b":
					Game.bedroom(inventory)
					return inventory
				elif RoomChoice == "k":
					Game.kitchen(inventory)
					return inventory
			if studychoice2 == "m":
				jp = random.randint(1,3)
				inventory[2] += jp
				inventory[0] -= 2
				print(f"You worked with medium effort!\nYour Job Performace is {inventory[2]} and your Executive Function points are at {inventory[0]}\n")
				RoomChoice = input(f"What room do you want to go to?\nthe Kitchen (k)\nor the Bedroom (b)\n")
				if RoomChoice == "b":
					Game.bedroom(inventory)
					return inventory
				elif RoomChoice == "k":
					Game.kitchen(inventory)
					return inventory
			if studychoice2 == "l":
				inventory[2] += 1
				inventory[0] -= 1
				print(f"You worked with low effort!\nYour Job Performace is {inventory[2]} and your Executive Function points are at {inventory[0]}\n")
				RoomChoice = input(f"What room do you want to go to?\nthe Kitchen (k)\nor the Bedroom (b)\n")
				if RoomChoice == "b":
					Game.bedroom(inventory)
					return inventory
				elif RoomChoice == "k":
					Game.kitchen(inventory)
					return inventory
		elif studychoice1 == "l":
			RoomChoice = input(f"What room do you want to go to?\nthe Kitchen (k)\nor the Bedroom (b)\n")
			if RoomChoice == "b":
				Game.bedroom(inventory)
			elif RoomChoice == "k":
				Game.kitchen(inventory)
	def livingroom(inventory):
		Game.save()
		Game.load()
		choice = input(f"\nWelcome to the Living room!\nYou see a TV and a Sofa!\nYou can:\nnap (n): +1 to 4 EF Points\nWatch TV (tv): -1 to +5 EF Points\nor leave (l)\n")
		if choice == "n":
			hours = random.randint(1,4)
			print("napping...\n"*hours)
			inventory[0] += hours
			print(f"Executive Function Points: {inventory[0]}")
			RoomChoice = input(f"Would you like to go to the Kitchen (k)\nor the Bedroom (b)\n")
			if RoomChoice == "k":
				Game.kitchen(inventory)
			elif RoomChoice == "b":
				Game.bedroom(inventory)
		elif choice == "tv":
			tv = random.randint(-1,5)
			inventory[0] += tv
			print(f"Executive Funciton Points: {inventory[0]}")
			RoomChoice = input(f"Would you like to go to the Kitchen (k)\nor the Bedroom (b)\n")
			if RoomChoice == "k":
				Game.kitchen(inventory)
			elif RoomChoice == "b":
				Game.bedroom(inventory)
		elif choice == "l":
			RoomChoice = input(f"Would you like to go to the Kitchen (k)\nor the Bedroom (b)\n")
			if RoomChoice == "k":
				Game.kitchen(inventory)
			elif RoomChoice == "b":
				Game.bedroom(inventory)
	def kitchen(inventory):
		Game.save()
		Game.load()
		choice = input(f"Welcome to the Kitchen!\nYou see a fridge and a stove!\nWould you like to make food (m): -2 EF points, +2 Health\nOrder food (o): -1 Health\nor leave (l)\n")
		if choice == "m":
			inventory[5] = True
			inventory[3] += 2
			inventory[0] -= 2
			print(f"You have made some good food and enjoyed it.")
			RoomChoice = input(f"Would you like to go to the Livingroom (l)\nor the Study (s)\n")
			if RoomChoice == "l":
				Game.livingroom(inventory)
			elif RoomChoice == "s":
				Game.study(inventory)
		elif choice == "o":
			inventory[5] = True
			inventory[3] -= 1
			print(f"You ordered food and enjoyed it.")
			RoomChoice = input(f"Would you like to go to the Livingroom (l)\nor the Study (s)\n")
			if RoomChoice == "l":
				Game.livingroom(inventory)
			elif RoomChoice == "s":
				Game.study(inventory)
		elif choice == "l":
			RoomChoice = input(f"Would you like to go to the Livingroom (l)\nor the Study (s)\n")
			if RoomChoice == "l":
				Game.livingroom(inventory)
			elif RoomChoice == "s":
				Game.study(inventory)
	def main():
	#starting game
		EFpoints = 10
		newday = True
		jobPerformace = 5
		health = 5
		daycount = 0
		hbtktd = False
		inventory = [EFpoints, newday, jobPerformace, health, daycount, hbtktd]
		startchoice = input("""
Hello! Welcome to the Work Week Simulator
To win the Work Week Simulator, you need to get through a week without getting Burnt Out.
You are considered "Burnt Out" if you start and end the day with 0 Executive Function Points.
	If you would like to begin please press 'y'.
	If you would like to quit you can press 'q'.
""")
		while startchoice != "q":
			if startchoice == "y":
				startchoice = ''
				print("""Here is a Map to help you:
____________________
|         |         |
| Kitchen | Living  |
|         |  Room   |
|_________|_________|
|         |         |
|  Study  | Bedroom |
|         |         |
|_________|_________|""")
			Game.bedroom(inventory)
	def save():
		with open('text_game.dat','wb') as file:
			game = pickle.dump(Game,file)
	def load():
		try:
			with open("tex_game.dat","rb") as file:
				Game = pickle.load(file)
		except FileNotFoundError:
			print("")