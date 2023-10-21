from cmu_graphics import *

def onMouseMove(x, y):
    app.fondo = 'negro'

Rótulo('sistema solar', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))
mercurio = Grupo(
    Círculo(200, 200, 45, relleno=None, borde='grisOscuro'),
    Círculo(200, 155, 5, relleno='marron'))
venus = Grupo(
    Círculo(200, 200, 70, relleno=None, borde='grisOscuro'),
    Círculo(200, 130, 8, relleno='naranja'))
tierra = Grupo(
    Círculo(200, 200, 95, relleno=None, borde='grisOscuro'),
    Círculo(200, 105, 8, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )
tierra.dirección = 'sentido-horario'

marte = Grupo(
    Círculo(200, 200, 120, relleno=None, borde='grisOscuro'),
    Círculo(200, 82.5, 10, relleno='rojoOscuro'))
jupiter = Grupo(
    Circulo(200,200,145,relleno=None ,borde='grisOscuro'),
    Circulo(200,55,16,relleno=gradiente('turquesaPalido','salmonClaro',inicio ='superior'))
)
urano = Grupo(
    Círculo(200, 200, 170, relleno=None, borde='grisOscuro'),
    Círculo(200, 30, 12, relleno='grisClaro'))



def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'

    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    
    

    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        marte.rotarAngulo += 2
        urano.rotarAngulo -= 4
        mercurio.rotarAngulo -=1
        venus.rotarAngulo += 3.5
        jupiter.rotarAngulo -=2.5
    else:
        tierra.rotarÁngulo -= 3
        marte.rotarAngulo -= 2
        urano.rotarAngulo += 4
        mercurio.rotarAngulo += 1      
        venus.rotarAngulo -= 3.5
        jupiter.rotarAngulo +=2.5
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()