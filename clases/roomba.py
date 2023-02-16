from tkinter import *

class Habitacion:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Mueble:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

def area(base, altura):
    a = base * altura
    return a

def base(x0, x1):
    b = x1 - x0
    return b

def altura(y0, y1):
    h = y1 - y0
    return h