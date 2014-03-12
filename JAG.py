from Tkinter import Tk, Canvas, PhotoImage

#Copyright Joshua Chin, contact at JoshuaRChin@gmail.com

__all__ = ["canvas"]
__authors__ = ["Joshua Chin"]


class canvas:

    def __init__(self, width, height):
        if type(width) != int:
            raise TypeError("Width must be an integer, recieved: %s"%width)
        if type(height) != int:
            raise TypeError("Height must be an integer, recieved: %s"%height)
        window = Tk()
        canvas = Canvas(window, width=width, height=height, bg="#000000")
        canvas.pack()
        image = PhotoImage(width=width, height=height)
        canvas.create_image((width//2, height//2), image=image, state="normal")

        self.width = width
        self.height = height
        self.canvas = canvas
        self.image = image
        
    def clear(self, r, g, b):
        color = rgb_to_hex(r,g,b)
        for x in range(self.width):
            for y in range(self.height):
                self.image.put(color, (x,y))
    
    def put(self, x, y, r, g, b):
        if type(x) != int:
            raise TypeError("x must be an integer, recieved: %s"%x)
        if type(y) != int:
            raise TypeError("y must be an integer, recieved: %s"%y)
        if not (0<=x<self.width):
            raise ValueError(
                "x must be between 0 and %s, recieved: %s"%(self.width, x))
        if not (0<=y<self.height):
            raise ValueError(
                "y must be between 0 and %s, recieved: %s"%(self.height, y))
        self.image.put(rgb_to_hex(r,g,b),(x,y))

    def display(self):
        self.canvas.update()

def rgb_to_hex(r,g,b):
    if type(r) != int:
        raise TypeError("r must be an integer, recieved: %s"%r)
    if type(g) != int:
        raise TypeError("g must be an integer, recieved: %s"%g)
    if type(b) != int:
        raise TypeError("b must be an integer, recieved: %s"%b)
    if not (0<=r<256):
        raise ValueError("r must be between 0 and 256, recieved: %s"%r)
    if not (0<=g<256):
        raise ValueError("g must be between 0 and 256, recieved: %s"%g)
    if not (0<=b<256):
        raise ValueError("b must be between 0 and 256, recieved: %s"%b)
    integer = r<<16 | g<<8 | b
    hexidecimal = hex(integer)
    return "#" + hexidecimal[2:] 
