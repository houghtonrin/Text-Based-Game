import bedroom
def main():
	#starting game
	startchoice = input("Hello! Welcome to the Work Week Simulator.\n\tIf you would like to begin please press 'y'.\n\tIf you would like to know more information please press 'i'.\n\tIf at any point you would like to quit you can press 'q'.\n")
	while startchoice != "q":
		if startchoice == "y":
			startchoice = ''
			bedroom.bedroom()
		elif startchoice == "i":
			print(f"This game is a representation of difficulties some people may face while trying to function like a \"normal\" adult")
			startchoice = input("\tIf you would like to begin please press 'y'.\n\tIf you would like to know more information please press 'i'.\n\tIf at any point you would like to quit you can press 'q'.\n")
