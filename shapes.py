# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 00:21:40 2022

@author: USER
"""
#checking if we use Python 3 version 
try:
    from tkinter import Tk, Canvas, BOTH
except ImportError:
    raise Exception("tkinter did not import successfully - check you are running Python 3 and that tkinter is available.")

import random

#create class for canvas 
class Paper():
    
    tk = None 
    #constractor 
    #self variable we can acess the attributes and method in the class
    def __init__(self, width = 600, height = 600):
        """
        Create a Paper object which is required to draw shapes onto.

        Args:
           width (int): The width of the display. Defaults to 600.
           height (int): The height of the display. Defaults to 600.

        Returns:
           Paper: A Paper object
        """
        #checking if we have 1 paper 
        if Paper.tk is not None:
            raise Exception("Error: Paper has already been created, there can be only one.")

        try:
            Paper.tk = Tk()
        except ValueError:
            raise Exception("Error: could not instantiate tkinter object")
        
        #setting atrributes 
        Paper.tk.title("Drawing shapes")
        Paper.tk.geometry(str(width)+"x"+str(height))
        Paper.tk.paper_width = width
        Paper.tk.paper_height = height

        # Create a tkinter canvas object to draw on
        Paper.tk.canvas = Canvas(Paper.tk)
        Paper.tk.canvas.pack(fill=BOTH, expand=1)
        
    def display(self):
        """
        display the paper 
        """
        Paper.tk.mainloop()
#create class for geometry shapes 
class Shape():
    #constractor 
    def __init__(self, width = 50, height = 50, x  = None, y = None, color = "black"):
        """
        Creates a generic 'shape' which contains properties common to all
        shapes such as height, width, x y coordinates and colour.

           Args:
               width (int): The width of the shape. Defaults to 50.
               height (int): The height of the shape. Defaults to 50.
               x (int): The x position of the shape. If None, the x position will be the middle of the screen. Defaults to None.
               y (int): The y position of the shape. If None, the y position will be the middle of the screen. Defaults to None.
               color (string): The color of the shape. Defaults to "black"
        """
        #checking if the paper is created ones 
        if Paper.tk is None:
           raise Exception("A Paper object has not been created. There is nothing to draw on.")
        
        #setting attributes 
        self.height = height
        self.width = width
        self.color = color
        
        #put the shape in the center if no coordinates are provided
        if x is None:
            self.x = (Paper.tk.paper_width/2) - (self.width/2)
        else:
            self.x = x
        if y is None:
            self.y = (Paper.tk.paper_height / 2) - (self.height / 2)
        else:
            self.y = y
        
    # This is an internal method not meant to be called by users
    def _location(self):
       """
       Internal method used by the class to get the location
       of the shape. 
       """
       x1 = self.x
       y1 = self.y
       x2 = self.x + self.width
       y2 = self.y + self.height
       return [x1, y1, x2, y2]
    #randomly generate the shapes looks 
    def randomize(self, smallest = 20, largest = 200):
        """
         Randomly generates width, height, position and colour for a shape. 
    
         Args:
             smallest (int): The smallest the shape can be. Defaults to 20
             largest (int): The largest the the shape can be. Defaults to 200.
    
        """
        self.width = random.randint(smallest, largest)
        self.height = random.randint(smallest, largest)
        
        self.x = random.randint(0, Paper.tk.paper_width.width)
        self.y = random.randint(0, Paper.tk.paper_height.height)
        
        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])
    #setters
    def set_width(self, width):
        """
        Sets the width of the shape.

        Args:
            width (int): The width of the shape
        """
        self.width = width
    def set_height(self, height):
       """
       Sets the height of the shape.
       
       Args:
           height (int): The height of the shape.
       """
       self.height = height
    def set_x(self, x):
        """
        Sets the x position of the shape
        
        Args:
            x (int): The x position for the shape.
        """
        self.x = x
    def set_y(self, y):
        """
        Sets the y position of the shape
        
        Args:
            y (int): The y position for the shape.
        """
        self.y = y
    def set_color(self, color):
       """
       Sets the colour of the shape
       
       Args:
           color (string): The color of the shape.
       """
       self.color = color
    def get_color(self):
        """
        Returns the colour of the shape
        
        Returns:
            color (string): The color of the shape
        """
        return self.color

#creating particular shapes and these are subclass of shapes class
# Rectangle class is a subclass of Shape
class Rectangle(Shape):
    
    #draw rectangural
    def draw(self):
        """
        Draws a rectangle on the canvas. 
        """
        x1, y1, x2, y2 = self._location()
        #draw the rect
        Paper.tk.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        
# Oval class is a subclass of Shape
class Oval(Shape):
    
    def draw(self):
        """
        Draws a oval on the canvas. 
        """
        x1, y1, x2, y2 = self._location()
        Paper.tk.canvas.create_oval(x1, y1, x2, y2, fill = self.color)
        
class Triangle(Shape):
    
    def __init__(self, x1 = 0, y1 = 0, x2 = 20, y2 = 0, x3 = 20, y3 = 20, color = "black"):
      """
       Overrides the Shape constructor because triangles require three
       coordinate points to be drawn, unlike rectangles and ovals.

       Args:
           x1 (int): The x position of the coordinate 1. Defaults to 0.
           y1 (int): The y position of the coordinate 1. Defaults to 0.
           x2 (int): The x position of the coordinate 2. Defaults to 20.
           y2 (int): The y position of the coordinate 2. Defaults to 0.
           x3 (int): The x position of the coordinate 3. Defaults to 20.
           y4 (int): The y position of the coordinate 3. Defaults to 20.
           color (string): The color of the shape. Defaults to "black"
      """
      #calling the shape constractor
      super().__init__(color = color)
      #remove height and width because triangle dont have them
      del self.height
      del self.width
      
      #adding the three cooradinates 
      self.x = x1
      self.y = y1
      self.x2 = x2
      self.y2 = y2
      self.x3 = x3
      self.y3 = y3
      
    def _location(self):
        """
        Internal method used by the class to get the location
        of the triangle. 
        """
        return [self.x, self.y, self.x2, self.y2, self.x3, self.y3]
    
    def draw(self):
        """
        Draws a Triangle on the canvas. 
        """
        x1, y1, x2, y2, x3, y3 = self._location()
        Paper.tk.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = self.color)
    def randomize(self):
        """
        Randomly chooses the location of all 3 triangle points as well
        as the colour of the triangle
        """
        self.x = random.randint(0, Paper.tk.paper_width)
        self.y = random.randint(0, Paper.tk.paper_height)
        self.x2 = random.randint(0, Paper.tk.paper_width)
        self.y2 = random.randint(0, Paper.tk.paper_height)
        self.x3 = random.randint(0, Paper.tk.paper_width)
        self.y3 = random.randint(0, Paper.tk.paper_height)
        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])
    def set_width(self, width):
        """
        Sets the width of the shape.

        Args:
            width (int): The width of the shape
        """
        self.width = width

    def set_height(self,height):
        """
        Sets the height of the shape.
        
        Args:
            height (int): The height of the shape.
        """
        self.height = height 
    def set_width(self, width):
        """
        Overrides the setter method for width

        Args:
            width (int): The width of the shape
        """
        raise Exception("Width cannot be defined for Triangle objects")

    def set_height(self, height):
        """
        Overrides the setter method for height

        Args:
            height (int): The height of the shape
        """
        raise Exception("Height cannot be defined for Triangle objects")
# "if you run this file (rather than importing it), run this demo script"
if __name__ == "__main__":
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
    oval2.set_color("fuchsia")
    oval2.set_x(30)
    oval2.set_y(90)
    oval2.draw()
    my_drawing.display()