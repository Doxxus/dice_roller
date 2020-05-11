import PySimpleGUI as gui
import roller as r

gui.theme('DarkPurple4')

# The Current Layout
layout = [	[gui.Text('Special Rolls:'), gui.Button('Roll with Advantage'), gui.Button('Roll with Disadvantage')],
			[gui.Text('Number of Dice to Roll'), gui.Spin([i for i in range(1,30)], initial_value=1, key='_spin_'), gui.Button(button_text='Reset')],
			[gui.Text('Rolls:'), gui.Button(button_text='D4', size=(5,1)), gui.Button(button_text='D6', size=(5,1)), gui.Button(button_text='D8', size=(5,1)), gui.Button(button_text='D10', size=(5,1)), gui.Button(button_text='D12', size=(5,1)), gui.Button(button_text='D20', size=(5,1)), gui.Button(button_text='D100', size=(5,1))], 
			[gui.Output(size=(58, 1), key = '_output_')],
			[gui.Button('QUIT')]]

# Create the Window
window = gui.Window('Simple Dice Roller', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	
	window.FindElement('_output_').Update('')
	
	if event in (None, 'Reset'):
		window.FindElement('_spin_').Update(value=1)
	
	elif event in (None, 'D4'):
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
	
	elif event in (None, 'QUIT'):	# if user closes window or clicks cancel
		break

window.close()