import PySimpleGUI as sg
import roller as r

sg.theme('DarkPurple4')	# Add a touch of color
# All the stuff inside your window.
layout = [	[sg.Text('Special Rolls:'), sg.Button('Roll with Advantage'), sg.Button('Roll with Disadvantage')],
			[sg.Text('Enter rolls here'), sg.InputText(), sg.Button('Roll Single'), sg.Button('Roll Multi')]]

# Create the Window
window = sg.Window('Simple Dice Roller', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()

	if event in (None, 'Roll Single'):
		print(values[0])
		roll = r.roll(values[0])
	
	elif event in (None, 'Roll with Advantage'):
		rolls = r.adv_roll("d20")
		
	elif event in (None, 'Roll with Disadvantage'):
		rolls = r.disadv_roll("d20")
	
	if event in (None, 'Cancel'):	# if user closes window or clicks cancel
		break
	
	print(event, values)

window.close()