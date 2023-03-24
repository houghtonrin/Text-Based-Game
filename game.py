import random
import game
def bedroom(inventory):
	DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	DayDescription = ["Time to start the week!", "Productive train! Next stop: YOU", "Hump Day! Let's Makle the most of it", "You can make it! I believe in you!", "Make sure that you wrap up your work week!"]
	if inventory[1]==True:
		inventory[1] = False
		print(f"Good Morning! It is {DAY[inventory[4]]}. {DayDescription[inventory[4]]}")
		inventory[4] += 1
		print(f"You have {inventory[0]} Executive Function Points.")
		BedChoice = input(f"Would you like to:\nget out of bed (o): -1 EF point\nor nap (n): +1 to 4 EF points\n")
		if BedChoice == "o":
			inventory[0] -= 1
			RoomChoice = input(f"Would you like to go to the Living Room (lr)\nor the Study (st)\n")
			if RoomChoice == "lr":
				game.livingroom(inventory)
				return inventory
			elif RoomChoice == "st":
				game.study(inventory)
				return inventory
		elif BedChoice =="n":
			hours = random.randint(1,4)
			print("napping...\n"*hours)
			inventory[0] += hours
			print(f"Executive Function Points: {inventory[0]}")
			RoomChoice = input(f"Would you like to go to the Living Room (lr)\nor the Study (st)\n")
			if RoomChoice == "lr":
				game.livingroom(inventory)
				return inventory
			elif RoomChoice == "st":
				game.study(inventory)
				return inventory
	elif inventory[1]==False:
		BedChoice = input(f"Welcome to the Bedroom! You see a bed, in a room! Would you like to:\nleave (l)\nnap: +1 to 4 EF Points (n)\nor sleep: start new day(s)")
		if BedChoice == "l":
			RoomChoice = input("\nWhat Room do you want to go to?\nLiving Room (lr)\nStudy (st)\n")
			if RoomChoice == "lr":
				game.livingroom(inventory)
			if RoomChoice == "st":
				game.study(inventory)
		elif BedChoice == "n":
			hours = random.randint(1,4)
			print("napping...\n"*hours)
			inventory[0] += hours
			RoomChoice = input("\nWhat Room do you want to go to?\nLiving Room (lr)\nStudy (st)\n")
			if RoomChoice == "lr":
				game.livingroom(inventory)
			if RoomChoice == "st":
				game.study(inventory)
		elif BedChoice == "s":
			game.bedroom(inventory)
def study(inventory):
	studychoice1 = input(f"Welcome to the Study!\nYou see a computer on a desk with a chair.\n Would you like to use it (u)\n or leave (l)")
	if studychoice1 == "u":
		studychoice2 = input(f"Would you like to work with high effort: +1 to 5 Job Performance , -3 EF Points (h)\n Work with medium effort: +1 to 3 Job Performance, -2 EF Points (m)\n or Work with Low Effort: +1 Job Performance, -1 EF Point (l)\nIf you would like to leave type q\n")
		if studychoice2 == "h":
			jp = random.randint(1,5)
			inventory[2] += jp
			inventory[0] -= 3
			print(f"You worked with high effort!\n Your Job Performace is {inventory[2]} and your Executive Function points are at {inventory[0]}\n")
			RoomChoice = input(f"What room do you want to go to?\n the Kitchen (k)\n or the Bedroom (b)\n")
			if RoomChoice == "b":
				game.bedroom(inventory)
				return inventory
			elif RoomChoice == "k":
				game.kitchen(inventory)
				return inventory
		if studychoice2 == "m":
			jp = random.randint(1,3)
			inventory[2] += jp
			inventory[0] -= 2
			print(f"You worked with medium effort!\n Your Job Performace is {inventory[2]} and your Executive Function points are at {inventory[0]}\n")
			RoomChoice = input(f"What room do you want to go to?\n the Kitchen (k)\n or the Bedroom (b)\n")
			if RoomChoice == "b":
				game.bedroom(inventory)
				return inventory
			elif RoomChoice == "k":
				game.kitchen(inventory)
				return inventory
		if studychoice2 == "l":
			inventory[2] += 1
			inventory[0] -= 1
			print(f"You worked with low effort!\n Your Job Performace is {inventory[2]} and your Executive Function points are at {inventory[0]}\n")
			RoomChoice = input(f"What room do you want to go to?\n the Kitchen (k)\n or the Bedroom (b)\n")
			if RoomChoice == "b":
				game.bedroom(inventory)
				return inventory
			elif RoomChoice == "k":
				game.kitchen(inventory)
				return inventory
	elif studychoice1 == "l":
		RoomChoice = input(f"What room do you want to go to?\n the Kitchen (k)\n or the Bedroom (b)\n")
		if RoomChoice == "b":
			game.bedroom(inventory)
		elif RoomChoice == "k":
			game.kitchen(inventory)
def livingroom(inventory):
	choice = (f"Welcome to the Living room!\n You see a TV and a Sofa!\n You can:\n nap (n): +1 to 4 EF Points\nWatch TV (tv): -1 to +5 EF Points\nor leave (l)")
	if choice == "n":
		hours = random.randint(1,4)
		print("napping...\n"*hours)
		inventory[0] += hours
		print(f"Executive Function Points: {inventory[0]}")
		RoomChoice = input(f"Would you like to go to the Kitchen (k)\nor the Bedroom (b)\n")
		if RoomChoice == "k":
			game.kitchen(inventory)
		elif RoomChoice == "b":
			game.bedroom(inventory)
	elif choice == "tv":
		tv = randint(-1,5)
		inventory[0] += tv
		print(f"Executive Funciton Points: {inventory[0]}")
		RoomChoice = input(f"Would you like to go to the Kitchen (k)\nor the Bedroom (b)\n")
		if RoomChoice == "k":
			game.kitchen(inventory)
		elif RoomChoice == "b":
			game.bedroom(inventory)
	elif choice == "l":
		RoomChoice = input(f"Would you like to go to the Kitchen (k)\nor the Bedroom (b)\n")
		if RoomChoice == "k":
			game.kitchen(inventory)
		elif RoomChoice == "b":
			game.bedroom(inventory)
	print(f"{EFpoints}")
def kitchen(inventory):
	RoomChoice = ""
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
	If at any point you would like to quit you can press 'q'.
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
			game.bedroom(inventory)
		elif startchoice == "i":
			print(f"This game is a representation of difficulties some people may face while trying to function like a \"normal\" adult")
			startchoice = input("\tIf you would like to begin please press 'y'.\n\tIf you would like to know more information please press 'i'.\n\tIf at any point you would like to quit you can press 'q'.\n")