from clases.roomba import *

def main():
    habitacion = Habitacion(500, 630)
    mueble = Mueble(int(input("Escriba la coordenada x0: ")), int(input("Escriba la coordenada y0: ")), int(input("Escriba la coordenada x1: ")), int(input("Escriba la coordenada y1: ")))
    
    root = Tk()
    root.title("Roomba")
    root.resizable(1,1)
    root.config(bg="black")
    root.config(bd=60)

    habitacion_graf = Canvas(width=habitacion.width, height=habitacion.height, bg='white')
    habitacion_graf.pack()

    habitacion_graf.create_rectangle(mueble.x0, mueble.y0, mueble.x1, mueble.y1, fill='brown')

    root.mainloop()

    base_mueble = base(mueble.x0, mueble.x1)
    altura_mueble = altura(mueble.y0, mueble.y1)
    
    area_habitacion = area(habitacion.width, habitacion.height)
    area_mueble = area(base_mueble, altura_mueble)
    
    area_util = area_habitacion - area_mueble
    
    velocidad_cm_s = 1000
    tiempo = area_util / velocidad_cm_s
    minutos = int(tiempo/60)
    segundos = int(tiempo % 60)
    
    print("El tiempo que tardará en limpiar la habitación es de", minutos, "minutos", segundos, "segundos")