from tkinter import *

from Vector import *


class Star():
    
    def __init__(self, canvas, pos = (250,250), mass = 1000, radius = 20, color="yellow"):
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

if __name__ == '__main__':
    Vector()