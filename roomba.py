from tkinter import *

class Mueble:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

mueble = Mueble(input("Escriba la coordenada x0: "), input("Escriba la coordenada y0: "), input("Escriba la coordenada x1: "), input("Escriba la coordenada y1: "))

root = Tk()
root.title("Roomba")
root.resizable(1,1)
root.config(bg="black")
root.config(bd=60)

habitacion = Canvas(width=500, height=630, bg='white')
habitacion.pack()

mueble = habitacion.create_rectangle(mueble.x0, mueble.y0, mueble.x1, mueble.y1, fill='brown')

root.mainloop()
