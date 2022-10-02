from tkinter import *

from Vector import *


class Star():
    
    def __init__(self, canvas, pos = (250,250), mass = 1000000, radius = 20, color="yellow"):
        self.canvas = canvas
        self.pos = Vector(pos[0], pos[1])
        self.mass = mass
        self.radius = radius
        self.color = color
        self.create_star()
                
    def create_star(self):
        self.item = self.canvas.create_oval(self.pos.x - self.radius, self.pos.y-self.radius, self.pos.x+self.radius, self.pos.y + self.radius, fill = self.color, outline = "black")

    def set_radius(self, new_radius):
        self.radius = new_radius
        self.create_star()
        
    def calc_a_vector(self, as_pos, s_length):
        #G = 6.6743e-11
        G = 6.7e-9
        to_mid = self.pos-as_pos
        a = G*self.mass/(abs(to_mid))**2*s_length
        #print(Vector(a,a)*to_mid.norm())
        return to_mid.norm().scalar_m(a)
        

if __name__ == '__main__':
    Vector()