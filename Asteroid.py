from tkinter import *

from Vector import *


class Asteroid():
    def __init__(self, canvas, pos = (100,100), vel = (-100,-100), mass = 1, radius = 3, color="white"):
        self.canvas = canvas
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector(vel[0], vel[1])
        self.mass = mass
        self.radius = radius
        self.color = color
        
        self.create_asteroid()
        
    def create_asteroid(self):
        self.item = self.canvas.create_oval(self.pos.x - self.radius, self.pos.y-self.radius, self.pos.x+self.radius, self.pos.y + self.radius, fill = self.color, outline = "black")