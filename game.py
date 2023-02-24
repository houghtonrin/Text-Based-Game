import random
import game
def bedroom(EFpoints):
	newday = True
	DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	DayDescription = ["Time to start the week!", "Productive train! Next stop: YOU", "Hump Day! Let's Makle the most of it", "You can make it! I believe in you!", "Make sure that you wrap up your work week!"]
	daycount = 0
	if newday==True:
		newday = False
		print(f"Good Morning! It is {DAY[daycount]}. {DayDescription[daycount]}")
		daycount + 1
		print(f"You have {EFpoints} Executive Function Points.")
		BedChoice = input(f"Would you like to:\nget out of bed (o): -1 EF point\nor nap (n): +1 to 4 EF points\n")
		if BedChoice == "o":
			EFpoints = EFpoints-1
			RoomChoice = input(f"Would you like to go to the Living Room (lr)\nor the Study (st)\n")
			if RoomChoice == "lr":
				game.livingroom(EFpoints)
				return EFpoints
			elif RoomChoice == "st":
				game.study(EFpoints)
				return EFpoints
		elif BedChoice =="n":
			hours = random.randint(1,4)
			print("napping...\n"*hours)
			EFpoints = EFpoints + hours
			print(f"Executive Function Points: {EFpoints}")
			RoomChoice = input(f"Would you like to go to the Living Room (lr)\nor the Study (st)\n")
			if RoomChoice == "lr":
				game.livingroom(EFpoints)
				return EFpoints
			elif RoomChoice == "st":
				game.study(EFpoints)
				return EFpoints
	elif newday==False:
		BedChoice = input(f"Welcome to the Bedroom! You see a bed, in a room! Would you like to:\nleave (l)\nnap: +1 to 4 EF Points (n)\nsleep: start new day(s)\nor learn more (i)\n")
		if BedChoice == "l":
			RoomChoice = input("\nWhat Room do you want to go to?\nLiving Room (lr)\nStudy (s)\n")
			if RoomChoice == "lr":
				game.livingroom(EFpoints)
			if RoomChoice == "st":
				game.study(EFpoints)
		elif BedChoice == "n":
			hours = random.randint(1,4)
			print("napping...\n"*hours)
			EFpoints = EFpoints + hours
def study(EFpoints):
	studychoice1 = input(f"Welcome to the Study!\nYou see a computer on a desk with a chair.\n Would you like to use it?\n")
	if studychoice1 == "y":
		studychoice2 = input(f"Would you like to work with high effort: +1 to 5 Job Performance , -3 EF Points (h)\n Work with medium effort: +1 to 3 Job Performance, -2 EF Points (m)\n or Work with Low Effort: +1 Job Performance, -1 EF Point")
def livingroom(EFpoints):
	print("Livingroom to come")
	print(f"{EFpoints}")
def kitchen(EFpoints):
	print("Kitchen to come")
	print(f"{EFpoints}")
def main():
	#starting game
	EFpoints = 10
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
			game.bedroom(EFpoints)
		elif startchoice == "i":
			print(f"This game is a representation of difficulties some people may face while trying to function like a \"normal\" adult")
			startchoice = input("\tIf you would like to begin please press 'y'.\n\tIf you would like to know more information please press 'i'.\n\tIf at any point you would like to quit you can press 'q'.\n")
			#Living Room
			print(f"Welcome to the Living room!\n You see a TV and a Sofa!\n You can:\n nap (n): +1 to 4 EF Points\n or Watch TV (tv): -1 to +5 EF Points\n")
