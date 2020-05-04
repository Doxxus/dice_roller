import random as r

def roll(type):
	return r.randint(1, type)
		
def run():
	print("Shitty Dice Roller: \n")
	
	while(True):
		user_input = input("> ")
			
		f = open("roll.txt", "w")
		
		#Handles multi dice rolls (of the form xdy where x is the number of die and the y is the type of die)
		if(user_input[0].isdigit() and user_input.find("d") != -1):
			dindex = user_input.find("d")
			
			sum = 0
			num = user_input[:dindex]
			die = user_input[dindex+1:]	
			rolls = []
			
			for i in range(int(num)):
				rol = roll(int(die))
				sum += rol
				rolls.append(str(rol))
				
			print(sum)
			print(rolls)
				
			f.write(user_input + ": " + str(sum) + "\n")
			f.write(str(rolls))
			
		#Handles rolling with advantage	
		elif(user_input[0] == "a" and user_input[1] == "d"):
			die = user_input[2:]
			rol1 = roll(int(die))
			rol2 = roll(int(die))
			
			print(rol1)
			print(rol2)
			
			f.write("Advantage: \n")
			if(rol1 > rol2):
				f.write(user_input[1:] + ": *" + str(rol1) + "\n")
				f.write(user_input[1:] + ": " + str(rol2) + "\n")
				
			else:
				f.write(user_input[1:] + ": " + str(rol1) + "\n")
				f.write(user_input[1:] + ": *" + str(rol2) + "\n")
		
		#Handles rolling with disadvantage
		elif(user_input[0] == "d" and user_input[1] == "d"):
			die = user_input[2:]
			rol1 = roll(int(die))
			rol2 = roll(int(die))
			
			print(rol1)
			print(rol2)
			
			f.write("Disadvantage: \n")
			if(rol1 > rol2):
				f.write(user_input[1:] + ": " + str(rol1) + "\n")
				f.write(user_input[1:] + ": *" + str(rol2) + "\n")
				
			else:
				f.write(user_input[1:] + ": *" + str(rol1) + "\n")
				f.write(user_input[1:] + ": " + str(rol2) + "\n")
		
		#Handles rolling with a single die
		elif(user_input[0] == "d"):
			die = user_input[1:]
			rol = roll(int(die))
			print(rol)
			f.write(user_input + ": " + str(rol))

		#Quits the program
		elif(user_input[0] == "q"):
			break
		
		#Catch all
		else:
			print("Please enter a valid input of the form 'dx' (where x is an integer), or 'q' to quit")
			
		f.close()