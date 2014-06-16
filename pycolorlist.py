#import os to get directory names etc.
import os
#import tkinter and modules to make gui
from Tkinter import *
#random to choose the hex code components
import random

#Enter a hex colour code for the background on the terminal
file_name = raw_input('Enter a name for the file containing the list: ')
background_color = raw_input('Enter background color e.g #FFFFFF for white or #000000 for black: ')

#Generate a random hex colour code from the keys
keys = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
color_code_list = []
global line_colour
line_colour = '#000333'
def make_line_colour():
	global line_colour 
	line_colour = '#%s%s%s%s%s%s' % (random.choice(keys), random.choice(keys), random.choice(keys), random.choice(keys), random.choice(keys), random.choice(keys))

def add_color():
	color_code_list.append(line_colour)
	
def next_color():
	global line_colour
	make_line_colour()
	w.itemconfig(xy, fill=line_colour)
	w.itemconfig(ab, fill=line_colour)
	
def end_list():
	print color_code_list
	f = open('%s' % file_name, 'w')
	f.write('%s' % color_code_list)
	f.close

master = Tk()

make_line_colour()
w = Canvas(master, width=500, height=500)
w.grid(row=1, column=0)
w.create_rectangle(50, 25, 450, 350, fill=background_color)
w.create_rectangle(450, 0, 500, 500, fill='#000000')
xy = w.create_line(0, 100, 500, 0, fill=line_colour, dash=(4, 4), tags='xy')
ab = w.create_line(100, 0, 500, 500, fill=line_colour, width=3.0, tags='ab')

color_ok = Button(master, text='Add colour to list!', command=add_color)
color_ok.grid(row=0, column=0, sticky=E)

next_color = Button(master, text='View next colour?', command=next_color)
next_color.grid(row=0, column=1, sticky=W)

end_list = Button(master, text='End the list?', command=end_list)
end_list.grid(row=0, column=2, sticky=W)


mainloop()
