from tkinter import *

def crear_ventana(habitacion, mueble):
    root = Tk()
    root.title("Roomba")
    root.resizable(1,1)
    root.config(bg="black")
    root.config(bd=60)

    habitacion_graf = Canvas(width=habitacion.width, height=habitacion.height, bg='white')
    habitacion_graf.pack()

    habitacion_graf.create_rectangle(mueble.x0, mueble.y0, mueble.x1, mueble.y1, fill='brown')

    root.mainloop()

