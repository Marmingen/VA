from tkinter import *
from tkinter import ttk
from Star import Star
from Asteroid import *

def conf_space(space_canvas):
    space_canvas['height'] = 500
    space_canvas['width'] = 500
    space_canvas['borderwidth'] = 2
    space_canvas['relief'] = 'ridge'
    space_canvas['background'] = '#29292B'
    
    space_canvas.grid(column=0, row=0, rowspan = 3, columnspan=3,sticky=NW)
    
def conf_opt(option_frame):
    option_frame['height'] = 500
    option_frame['width'] = 150
    option_frame['padding'] = 5
    option_frame['borderwidth'] = 2
    option_frame['relief'] = 'ridge'

    option_frame.grid(column=3, row=0, rowspan = 3, columnspan=1,sticky=NE)

def main():

    root = Tk()

    top_frame = ttk.Frame(root)
    top_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    sqre_cnvas = Canvas(top_frame)
    conf_space(sqre_cnvas)
    
    option_frame = ttk.Frame(top_frame)
    conf_opt(option_frame)
    
    top_frame.columnconfigure(4, weight=1)
    top_frame.rowconfigure(3, weight=1)
    
    sun = Star(sqre_cnvas)
    ast = Asteroid(sqre_cnvas)
    
    button = ttk.Label(top_frame, text="hey")
    #button['text'] = "hey"

    button.grid(column=3,row=0)

    root.mainloop()
    
    
if __name__ == '__main__':
    main()