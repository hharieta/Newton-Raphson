from numpy import integer
import math
from math import e
from graficación2 import grafica as g

def funcion(x):
    # return 2 * x * math.sin(4 * x) - 2 * x**2 + 1
    # return (e**-x) - x
    return x**10 - 1

# primera derivada central
def derivada_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


# x0 valor inicial, es: tolerancia, imax: iteraciones máximas, it: inicio de iteración, ea: error relativo aproximado
def newtho_raphson(x0, es, imax, it, ea=integer.min):
    xr = x0
   
    while True:
        xr_anterior = xr
        xr = xr_anterior - (funcion(xr_anterior) / derivada_central(funcion, 1, 0.000001))
        print(xr)
        it += 1
        if xr != 0:
            ea = abs((xr - xr_anterior) / xr)

        # cuando se alcanza el valor máximo de iteraciones o el error relativo es menor al error esperado
        if ea < es or it >= imax:
            break

    return it, xr, es, ea


def main():
    init_value = float(input("valor inicial: "))
    tolerancia = float(input("toleracia: "))
    
    # valor inicial, tolerancia, iteraciones máximas, inicio de iteración, error relativo porcentaul aproximado (no necesario como argumento)
    list_result = newtho_raphson(init_value, tolerancia, 1000, 0)
    g(funcion, list_result[1])
    

    print("it \t raíz\t\t tolerancia\t error aproximado")
    print("{}\t {}\t {}\t {}".format(list_result[0], list_result[1], list_result[2], list_result[3]))


if __name__ == '__main__':
    main()