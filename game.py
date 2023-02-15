import random
import game
def bedroom():
	newday = True
	DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	DayDescription = ["Time to start the week!", "Productive train! Next stop: YOU", "Hump Day! Let's Makle the most of it", "You can make it! I believe in you!", "Make sure that you wrap up your work week!"]
	daycount = 0
	if newday==True:
		newday = False
		print(f"Good Morning! It is {DAY[daycount]}. {DayDescription[daycount]}")
		daycount + 1
		print(f"You have TK Executive Function Points.")
		BedChoice = input(f"Would you like to:\nget out of bed (o): -1 EF point\nor nap (n): +1 to 4 EF points\n")
	elif newday==False:
		BedChoice = input(f"Welcome to the Bedroom! You see a bed, in a room! Would you like to:\nleave (l)\nnap (n)\nsleep(s)\nor learn more (i)\n")
		if BedChoice == "l":
			RoomChoice = input("\nWhat Room do you want to go to?\nLiving Room (lr)\nStudy (s)\n")
			if RoomChoice == "lr":
				print("start living room")
			if RoomChoice == "s":
				print("start study")
		elif BedChoice == "n":
			hours = random.randint(1,4)
			print("napping...\n"*hours)
			print(f"{hours}")
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
			game.bedroom()
		elif startchoice == "i":
			print(f"This game is a representation of difficulties some people may face while trying to function like a \"normal\" adult")
			startchoice = input("\tIf you would like to begin please press 'y'.\n\tIf you would like to know more information please press 'i'.\n\tIf at any point you would like to quit you can press 'q'.\n")
			#Living Room
			print(f"Welcome to the Living room!\n You see a TV and a Sofa!\n You can:\n nap (n): +1 to 4 EF Points\n or Watch TV (tv): -1 to +5 EF Points\n")
