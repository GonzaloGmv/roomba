# roomba

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/GonzaloGmv/roomba.git)

### Integrantes

- Gonzalo Martinez
- Jose Zazo

### Resumen

Para este proyecto hemos realizado un roomba que se encuentra en una habitacion con un mueble, y reconoce los obstaculos para limpiar toda la sala de manera optima. Tambien calcula el area barrida y el tiempo que tarda en barrerla.

### Codigo

- Roomba

Aquí
```
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
```

- Ventana

```
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

```

- Cálculos
```
def area(base, altura):
    a = base * altura
    return a

def base(x0, x1):
    b = x1 - x0
    return b

def altura(y0, y1):
    h = y1 - y0
    return h

def calcular(habitacion, mueble):
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
```    

- Lanzador

```
from clases.roomba import *
from ventana import crear_ventana
from calculos import calcular

def main():
    habitacion = Habitacion(500, 630)
    mueble = Mueble(int(input("Escriba la coordenada x0: ")), int(input("Escriba la coordenada y0: ")), int(input("Escriba la coordenada x1: ")), int(input("Escriba la coordenada y1: ")))
    
    crear_ventana(habitacion, mueble)
    calcular(habitacion, mueble)
```

- Main

```
from lanzador import*

if __name__ == "__main__":
    main()
```

- Ejecución

Una vez el usuario haya dado las coordenas del mueble, se abrirá una interfaz gráfica con la habitación y el mueble creado.

![image](https://user-images.githubusercontent.com/91721237/223156475-942395f1-2f9f-4cd7-b928-ff03b0abf8de.png)

Después, el programa calculará el tiempo que tarda el roomba en limpiar la habitación, teniendo en cuenta el mueble.

![image](https://user-images.githubusercontent.com/91721237/223156774-675b3568-5e79-4475-b897-1000e9c8f898.png)

