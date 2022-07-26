from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy


def grafica(f, xr):
    mpl.rcParams['figure.dpi'] = 300  # puntos por pulgada
    mpl.rcParams['savefig.dpi'] = 300  # puntos por pulgada con lo que se guarda la grafica

    # Valores del eje X que toma el gráfico.
    x = numpy.linspace(-10, 15, 600)

    # Graficar función
    plt.plot(x, [f(i) for i in x])

    # Establecer el color de los ejes.
    plt.scatter(xr, 0, color='black')
    plt.axvline(x = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.axhline(y = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    
    plt.title('Newton-Raphson',
        fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["f(x)"])
    plt.grid(True)
    plt.axis([-3, 3, -5, 3])  # intervalos de los ejes de la grafica. Cambiar si es necesario
    # Guardar gráfico como imágen PNG.
    plt.savefig("output.png")
    # Mostrar gráfico.
    plt.show()
