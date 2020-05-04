import random as r

def get_roll(type):
	return r.randint(1, type)

def multi_roll(inp):
	f = open("roll.txt", "w")

	dindex = inp.find("d")
			
	sum = 0
	num = inp[:dindex]
	die = inp[dindex+1:]	
	rolls = []
			
	for i in range(int(num)):
		rol = get_roll(int(die))
		sum += rol
		rolls.append(str(rol))
				
	print(sum)
	print(rolls)
				
	f.write(inp + ": " + str(sum) + "\n")
	f.write(str(rolls))
	f.close()
	
	return sum, rolls
	
def adv_roll(inp):
	f = open("roll.txt", "w")

	die = inp[1:]
	rol1 = get_roll(int(die))
	rol2 = get_roll(int(die))
			
	rolls = []
			
	print(rol1)
	print(rol2)
			
	f.write("Advantage: \n")
	
	if(rol1 > rol2):
		f.write(inp + ": *" + str(rol1) + "\n")
		f.write(inp + ": " + str(rol2) + "\n")
		rolls += str(rol1)
		rolls += str(rol2)
				
	else:
		f.write(inp + ": " + str(rol1) + "\n")
		f.write(inp + ": *" + str(rol2) + "\n")
		rolls += str(rol2)
		rolls += str(rol1)
		
	f.close()
	
	return rolls
		
def disadv_roll(inp):
	f = open("roll.txt", "w")

	die = inp[1:]
	rol1 = get_roll(int(die))
	rol2 = get_roll(int(die))
	
	rolls = []
			
	print(rol1)
	print(rol2)
			
	f.write("Disadvantage: \n")
	
	if(rol1 > rol2):
		f.write(inp + ": " + str(rol1) + "\n")
		f.write(inp + ": *" + str(rol2) + "\n")
		rolls += str(rol2)
		rolls += str(rol1)
				
	else:
		f.write(inp + ": *" + str(rol1) + "\n")
		f.write(inp + ": " + str(rol2) + "\n")
		rolls += str(rol1)
		rolls += str(rol2)
		
	f.close()
	
	return rolls

def roll(inp):
	f = open("roll.txt", "w")
	
	die = inp[1:]
		
	rol = get_roll(int(die))
	print(rol)
	f.write(inp + ": " + str(rol))
	f.close()
	
	return rol

def run_console():
	print("Simple Dice Roller: \n")
	
	while True:
		user_input = input("> ")
		
		#Handles multi dice rolls (of the form xdy where x is the number of die and the y is the type of die)
		if(user_input[0].isdigit() and user_input.find("d") != -1):
			multi_roll(user_input)
			
		#Handles rolling with advantage	
		elif(user_input[0] == "a" and user_input[1] == "d"):
			adv_roll(user_input[1:])
			
		#Handles rolling with disadvantage
		elif(user_input[0] == "d" and user_input[1] == "d"):
			disadv_roll(user_input[1:])
		
		#Handles rolling with a single die
		elif(user_input[0] == "d"):
			roll(user_input)

		#Quits the program
		elif(user_input[0] == "q"):
			break
		
		#Catch all
		else:
			print("Please enter a valid input of the form 'dx' (where x is an integer), or 'q' to quit")