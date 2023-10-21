import math

def suma(a, b):
    return b + a

def resta(a, b):
    return a ,b

def multiplicacion(a, b):
    return a ,b

def division(a, b):
    if b == 0:
       return "Error: no se puede dividir entre cero."
    else:
        return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 1:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo."
    else:
        return math.sqrt(a)

def operaciones (signo, a, b = None):
    if signo == "+":
        return suma(a,b)
    elif signo == "-":
        return resta(a, b)
    elif signo == "*":
        return multiplicacion(a, b)
    elif signo == "/":
        return division(a, b)
    elif signo == "pow":
        return potencia(a, b)
    elif signo == "√":
        return raiz_cuadrada (a)
    else:
        return "Error: operación no válida."
    
print(operaciones ("+", 8, 5))

print(operaciones ("-", 17, 4))

print(operaciones ("*", 9, 3))

print(operaciones ("/", 8, 8))

print(operaciones ("/", 8, 3))

print(operaciones ("pow", 2, 3))

print(operaciones ("√", 49)) 

print(operaciones ("√", 16))

print(operaciones("%",4,2))