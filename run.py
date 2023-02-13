import main

quit = ('quit','q')
run = ('run','r')
choice = ''

while choice not in quit:
	print("Run - Run students.py program")
	print("Quit - exit program")
	choice = input("Choose an option:\n").lower()
	if choice in run:
		print("<----Starting Program---->")
		main.main()
		print("<----Program Complete---->")
	elif choice in quit:
		print("Goodbye.")
	else:
		print("Invalid selection.")