# roomba

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/GonzaloGmv/roomba.git)

### Resumen

Para este proyecto hemos realizado un roomba que se encuentra en una habitacion con un mueble, y reconoce los obstaculos para limpiar toda la sala de manera optima. Tambien calcula el area barrida.

### Codigo

- Roomba
```
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

habitacion = Habitacion(500, 630)
mueble = Mueble(int(input("Escriba la coordenada x0: ")), int(input("Escriba la coordenada y0: ")), int(input("Escriba la coordenada x1: ")), int(input("Escriba la coordenada y1: ")))

root = Tk()
root.title("Roomba")
root.resizable(1,1)
root.config(bg="black")
root.config(bd=60)

habitacion_graf = Canvas(width=habitacion.width, height=habitacion.height, bg='white')
habitacion_graf.pack()

mueble_graf = habitacion_graf.create_rectangle(mueble.x0, mueble.y0, mueble.x1, mueble.y1, fill='brown')

root.mainloop()

def area(base, altura):
    a = base * altura
    return a

def base(x0, x1):
    b = x1 - x0
    return b

def altura(y0, y1):
    h = y1 - y0
    return h

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

```

- Main

```

```
### Integrantes

- Gonzalo Martinez
- Jose Zazo
