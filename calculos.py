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