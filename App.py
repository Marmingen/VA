from tkinter import *
from tkinter import ttk
from Star import Star
from Asteroid import *
import random as r

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("star system")
        
        self.pause = True

        self.top_frame = ttk.Frame(self.root)
        self.top_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.sqre_cnvas = Canvas(self.top_frame)
        self.conf_space(self.sqre_cnvas)
        
        self.option_frame = ttk.Frame(self.top_frame)
        self.conf_opt(self.option_frame)
        
        self.top_frame.columnconfigure(5, weight=1)
        self.top_frame.rowconfigure(3, weight=1)
        
        self.set_star(Star(self.sqre_cnvas))
        self.asts = []
        
        self.days = 0
        self.day_label = self.sqre_cnvas.create_text(500, 500, text=f'Days: {self.days}', anchor='se', font='TkMenuFont', fill='white')
        
        self.ast_label = self.sqre_cnvas.create_text(8, 500, text=f'Asteroids: {len(self.asts)}', anchor='sw', font='TkMenuFont', fill='white')
        
        button = ttk.Button(self.option_frame, text="add random asteroid", command=self.add_random_ast)

        button.grid(column=3,row=0, columnspan=2)
        
        self.pause_btn = ttk.Button(self.option_frame, text="play",  command=self.flip_paus)
        
        self.pause_btn.grid(column=3, row=1, columnspan=2)
        
        self.restart_entry = ttk.Entry(self.option_frame)
        
        self.restart_entry.grid(column=4, row=2)
        
        self.restart_entry.insert(0, "10")
        
        restart_btn =  ttk.Button(self.option_frame, text="restart",  command=self.restart)

        restart_btn.grid(column=3, row=2)
        
        self.restart()

    def conf_space(self, space_canvas):
        space_canvas['height'] = 500
        space_canvas['width'] = 500
        space_canvas['borderwidth'] = 2
        space_canvas['relief'] = 'ridge'
        space_canvas['background'] = '#29292B'
        
        space_canvas.grid(column=0, row=0, rowspan = 3, columnspan=3,sticky=NW)
        
    def conf_opt(self, option_frame):
        option_frame['height'] = 500
        option_frame['width'] = 200
        option_frame['padding'] = 5
        option_frame['borderwidth'] = 2
        option_frame['relief'] = 'ridge'

        option_frame.grid(column=3, row=1, rowspan = 1, columnspan=2,sticky=NE)
        
        option_frame.columnconfigure(2, weight=1)
        option_frame.rowconfigure(6, weight=1)

    def step(self):
        if not self.pause:
            for ast in self.asts:
                ast.step()
                p = self.sqre_cnvas.coords(ast.item)
                collisions = self.sqre_cnvas.find_overlapping(p[0], p[1], p[2], p[3])
                collisions = list(collisions)
                collisions.remove(ast.item)
                
                if collisions:
                    coll_obj = [ast_o for ast_o in self.asts if ast_o.item in collisions]
                    for ast_ in coll_obj:
                        ast.collision(ast_)
                        
            p = self.sqre_cnvas.coords(self.star.item)
            collisions = self.sqre_cnvas.find_overlapping(p[0], p[1], p[2], p[3])
            collisions = list(collisions)
            collisions.remove(self.star.item)

            if collisions:
                coll_obj = [ast_o for ast_o in self.asts if ast_o.item in collisions]
                for ast_,ast_id in zip(coll_obj, collisions):
                    self.asts.remove(ast_)
                    self.sqre_cnvas.delete(ast_id)
            
            self.days += 1
            self.sqre_cnvas.itemconfigure(self.day_label, text = f'Days: {self.days}')
            
        self.sqre_cnvas.itemconfigure(self.ast_label, text = f'Asteroids: {len(self.asts)}')
        self.root.after(10, self.step)

    def start(self):
        self.step()
        self.root.mainloop()
        
    def flip_paus(self):
        self.pause = not self.pause
        if self.pause:
            s = "start"
        else:
            s = "pause"

        self.pause_btn.config(text=f'{s}')
    
    def set_star(self, star):
        self.star = star
    
    def add_ast(self):
        self.asts.append(Asteroid(self.sqre_cnvas, self.star, vel=(0,0)))
        
    def add_random_ast(self):
        self.asts.append(Asteroid(self.sqre_cnvas, self.star, (r.uniform(0,500), r.uniform(0,500)), vel=(r.uniform(-1,1), r.uniform(-1,1))))
        
    def restart(self):
        for ast in self.asts:
            self.sqre_cnvas.delete(ast.item)
        self.asts = []
        for i in range(int(self.restart_entry.get())):
            self.add_random_ast()
        

def main():

    app = App()
    app.start()

    
    
if __name__ == '__main__':
    main()