import math

def FUNCION(valor):
    return 2 * valor * math.sin(4* valor) - 2 * valor**2 + 1#LA ECUACION A RESOLVER ES 2x * sin(4x) - 2x² + 1

def DERIVADA(valor):
    return 2 * math.cos(4 * valor) - 4 * valor #SE CALCULA LA DERIVADA DE LA FUNCION, QUE ES 2 * cos(4x) - 4x

x0 = float(input(f"Dame el valor inicial de la iteracion: "))
Niteraciones = int(input(f"Dame el número de iteraciones: "))
print("NO. ITERACION           X_N")
contador = 1
while Niteraciones>contador:
    x1 = x0 - FUNCION(x0)/DERIVADA(x0)
    error = abs(x0-x1) 
    x0 = x1 
    contador +=1
    print(f"{contador}  _ _ _ _ _ {x1}")
print(f"El valor aproximado de la raíz es {x0}")