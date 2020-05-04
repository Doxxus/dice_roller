import PySimpleGUI as sg
import roller as r

sg.theme('DarkPurple4')	# Add a touch of color
# All the stuff inside your window.
layout = [	[sg.Text('Special Rolls:'), sg.Button('Roll with Advantage'), sg.Button('Roll with Disadvantage')],
			[sg.Text('Rolls:'), sg.Button('D4'), sg.Button('D6'), sg.Button('D8'), sg.Button('D10'), sg.Button('D12'), sg.Button('D20'), sg.Button('D100')],
			[sg.Text('Number of Dice to Roll'), sg.Spin([i for i in range(1,30)], initial_value=1)],
			[sg.Output(size=(50, 1))]]

# Create the Window
window = sg.Window('Simple Dice Roller', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()

	if event in (None, 'D4'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d4")
		else:
			r.roll("d4")
	
	elif event in (None, 'D6'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d6")
		else:
			r.roll("d6")
	
	elif event in (None, 'D8'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d8")
		else:
			r.roll("d8")
			
	elif event in (None, 'D10'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d10")
		else:
			r.roll("d10")
			
	elif event in (None, 'D12'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d12")
		else:
			r.roll("d12")
			
	elif event in (None, 'D20'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d20")
		else:
			r.roll("d20")
			
	elif event in (None, 'D100'):
		if(values[0] != 1):
			r.multi_roll(str(values[0]) + "d100")
		else:
			r.roll("d100")
	
	elif event in (None, 'Roll with Advantage'):
		r.adv_roll("d20")
		
	elif event in (None, 'Roll with Disadvantage'):
		r.disadv_roll("d20")
	
	elif event in (None, 'Cancel'):	# if user closes window or clicks cancel
		break
	
	print(event, values)

window.close()