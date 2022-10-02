from tkinter import *

from Vector import *

import random as r


class Asteroid():
    def __init__(self, canvas, star, pos = (150,50), vel = (-1,1), mass = 1, radius = 3, color="white"):
        self.canvas = canvas
        self.star = star
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector(vel[0], vel[1])
        self.mass = mass
        self.radius = radius
        self.color = color
        
        self.step_length = 60*60*24
        
        self.create_asteroid()
        
    def create_asteroid(self):
        self.item = self.canvas.create_oval(self.pos.x - self.radius, self.pos.y-self.radius, self.pos.x+self.radius, self.pos.y + self.radius, fill = self.color, outline = "black")
    
    
    
    def accelerate(self, star):
        self.vel = self.vel + star.calc_a_vector(self.pos, self.step_length)
    
    def collision(self, other):
        self.vel = self.vel + (other.pos-self.pos).scalar_m((other.vel-self.vel)*(other.pos-self.pos)/(abs(other.pos-self.pos))**2)
        
    
    #def delete(self)
    
    def step(self):
        self.accelerate(self.star)
        self.pos = self.pos + self.vel
        self.canvas.moveto(self.item, int(self.pos.x+0.5), int(self.pos.y+0.5))
        