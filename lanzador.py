from clases.roomba import *
from ventana import crear_ventana
from calculos import calcular

def main():
    habitacion = Habitacion(500, 630)
    mueble = Mueble(int(input("Escriba la coordenada x0: ")), int(input("Escriba la coordenada y0: ")), int(input("Escriba la coordenada x1: ")), int(input("Escriba la coordenada y1: ")))
    
    crear_ventana(habitacion, mueble)
    calcular(habitacion, mueble)