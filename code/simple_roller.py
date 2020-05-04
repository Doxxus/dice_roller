import PySimpleGUI as gui
import roller as r

sg.theme('DarkPurple4')	# Add a touch of color
# All the stuff inside your window.
layout = [	[gui.Text('Special Rolls:'), gui.Button('Roll with Advantage'), gui.Button('Roll with Disadvantage')],
			[gui.Text('Rolls:'), gui.Button('D4'), gui.Button('D6'), gui.Button('D8'), gui.Button('D10'), gui.Button('D12'), gui.Button('D20'), gui.Button('D100')],
			[gui.Text('Number of Dice to Roll'), gui.Spin([i for i in range(1,30)], initial_value=1)],
			[gui.Output(size=(50, 1), key = '_output_')]]

# Create the Window
window = gui.Window('Simple Dice Roller', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	
	window.FindElement('_output_').Update('')
	
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

window.close()