import random
def bedroom():
	#Bedroom Description
	newday = True
	DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	DayDescription = ["Time to start the week!", "Productive train! Next stop: YOU", "Hump Day! Let's Makle the most of it", "You can make it! I believe in you!", "Make sure that you wrap up your work week!"]
	daycount = 0
	if newday==True:
		print(f"Good Morning! It is {DAY[daycount]}. {DayDescription[daycount]}")
		daycount + 1
		print(f"You have 10 Executive Function Points.")
		BedChoice = input(f"Would you like to:\nget out of bed (o): -1 EF point\nor nap (n): +1 to 4 EF points\n")
	elif newday!=True:
		BedChoice = input(f"Welcome to the Bedroom! You see a bed, in a room! Would you like to:\nleave (l)\nnap (n)\nsleep(s)\nor learn more (i)")
		if BedChoice == "l":
			RoomChoice = input("\tWhat Room do you want to go to?\nLiving Room (lr)\nStudy (s)")
			if RoomChoice == "lr":
				print("start living room")
			if RoomChoice == "s":
				print("start study")
		elif BedChoice == "n":
			hours = random.range(1,4)
			print("napping..."*hours)
			print("hours")