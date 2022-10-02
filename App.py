from tkinter import *
from tkinter import ttk
from Star import Star
from Asteroid import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("star system")
        
        self.pause = False

        self.top_frame = ttk.Frame(self.root)
        self.top_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.sqre_cnvas = Canvas(self.top_frame)
        self.conf_space(self.sqre_cnvas)
        
        self.option_frame = ttk.Frame(self.top_frame)
        self.conf_opt(self.option_frame)
        
        self.top_frame.columnconfigure(4, weight=1)
        self.top_frame.rowconfigure(3, weight=1)
        
        self.set_star(Star(self.sqre_cnvas))
        self.asts = []
        self.add_ast()
        
        button = ttk.Label(self.top_frame, text="hey")

        button.grid(column=3,row=0)

    def conf_space(self, space_canvas):
        space_canvas['height'] = 500
        space_canvas['width'] = 500
        space_canvas['borderwidth'] = 2
        space_canvas['relief'] = 'ridge'
        space_canvas['background'] = '#29292B'
        
        space_canvas.grid(column=0, row=0, rowspan = 3, columnspan=3,sticky=NW)
        
    def conf_opt(self, option_frame):
        option_frame['height'] = 500
        option_frame['width'] = 150
        option_frame['padding'] = 5
        option_frame['borderwidth'] = 2
        option_frame['relief'] = 'ridge'

        option_frame.grid(column=3, row=0, rowspan = 3, columnspan=1,sticky=NE)

    def start(self):
        self.step()
        self.root.mainloop()
        
    def step(self):
        if not self.pause:
            for ast in self.asts:
                ast.step()
                
        self.root.after(10, self.step)
    
    def set_star(self, star):
        self.star = star
    
    def add_ast(self):
        self.asts.append(Asteroid(self.sqre_cnvas, self.star))

def main():

    app = App()
    app.start()

    
    
if __name__ == '__main__':
    main()