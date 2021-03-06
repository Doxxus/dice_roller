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
	
	if event in ('Reset'):
		window.FindElement('_spin_').Update(value=1)
	
	elif event in ('D4'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d4")
		else:
			r.roll("d4")
	
	elif event in ('D6'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d6")
		else:
			r.roll("d6")
	
	elif event in ('D8'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d8")
		else:
			r.roll("d8")
			
	elif event in ('D10'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d10")
		else:
			r.roll("d10")
			
	elif event in ('D12'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d12")
		else:
			r.roll("d12")
			
	elif event in ('D20'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d20")
		else:
			r.roll("d20")
			
	elif event in ('D100'):
		if(values['_spin_'] != 1):
			r.multi_roll(str(values['_spin_']) + "d100")
		else:
			r.roll("d100")
	
	elif event in (None, 'Roll with Advantage'):
		r.adv_roll("d20")
		
	elif event in (None, 'Roll with Disadvantage'):
		r.disadv_roll("d20")
	
	elif event in (None, 'QUIT'):	# if user closes window or clicks cancel
		break

window.close()