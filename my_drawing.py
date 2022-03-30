# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 01:58:22 2022

@author: USER
"""

from shapes import Paper, Triangle, Rectangle, Oval
my_drawing = Paper()
  
#random size and location
tri = Triangle()
tri.randomize()
tri.draw()
  
rect = Rectangle(height=40, width=90, x=110, y=20, color="blue")
rect.draw()
  
oval = Oval()
oval.draw()
  
#oval with setters
oval2 = Oval()
oval2.set_height(200)
oval2.set_width(100)
oval2.set_color("red")
oval2.set_x(30)
oval2.set_y(90)
oval2.draw()
my_drawing.display()


