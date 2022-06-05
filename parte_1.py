import numpy as np
from scipy import stats
import os


filename= os.getcwd() + '\Tarea3\Conjunto_datos_tarea2.csv' # Cargar datos, colocar codigo junto al archivo de los datos


def cargarDatos(direccion,numpy_array): # numpy_array true para obtener la salida en numpy_array sino array normal

    datos0=np.genfromtxt(direccion,delimiter=';',skip_header=1, usecols = range(1,2))  
    datos1=np.genfromtxt(direccion,delimiter=';',skip_header=1, usecols = range(2,3))
    datos2=np.genfromtxt(direccion,delimiter=';',skip_header=1, usecols = range(3,4))
    if(numpy_array):
        return datos0, datos1, datos2
    else:
        return datos0.tolist, datos1.tolist, datos2.tolist


def calcularPruebasT(datos1,datos2,datos3,hip_Nula,alter):
    
    # Datos iniciales
    test1 = stats.ttest_1samp(a = datos1, popmean = hip_Nula, alternative=alter)

    # Primer cambio
    test2 = stats.ttest_1samp(a = datos2, popmean = hip_Nula, alternative=alter)

    # Segundo cambio
    test3 = stats.ttest_1samp(a = datos3, popmean = hip_Nula, alternative=alter)

    return test1,test2,test3


def verificarConPruebasT(datos1,hip_Nula,alter):
    
    # Prueba con la hi
    test1 = stats.ttest_1samp(a = datos1, popmean = hip_Nula, alternative=alter)

    return test1


def comparacionConPruebasT(datos1,datos2):
    
    # Se asume que la poblacion varia para cada uno de los set de datos ingresados
    comp1 = stats.ttest_ind(a=datos1, b=datos2, equal_var=False)

    return comp1


# Obtener los datos en listas o numpy_array, ingresar False para lista normal
iniciales, primer_cambio, segundo_cambio = cargarDatos(filename, True)

# Comprobamos por medio de la media si cada conjunto de datos está por encima del %70
print("Comprobamos por medio de la media si cada conjunto de datos está por encima del %70")
print("Media para los datos iniciales: ",iniciales.mean())
print("Media para los datos del primer cambio: ",primer_cambio.mean())
print("Media para los datos del segundo cambio: ",segundo_cambio.mean())

# Calculamos el numero de datos por muestra
n = len(iniciales)

# Proponemos segun el razonamiento del grupo la hipotesis nula
H0 = 70 

# Inicio de pruebas T
pruebasT = calcularPruebasT(iniciales,primer_cambio,segundo_cambio,H0,"greater")
prueba1 = verificarConPruebasT(iniciales,H0,"greater")
prueba2 = verificarConPruebasT(primer_cambio,H0,"greater")
prueba3 = verificarConPruebasT(segundo_cambio,H0,"greater")

print("El valor 'p' para la hipotesis: iniciales > 70 es ", prueba1.pvalue)
print("El valor 'p' para la hipotesis: primer cambio > 70 es ", prueba2.pvalue)
print("El valor 'p' para la hipotesis: segundo cambio > 70 es ", prueba3.pvalue)

# Verificar si el primer cambio cumple con el %75 de rendimiento prometido por medio de la prueba de hipotesis T

# Reajustamos la hipotesis nula a 75
H0 = 75

# Iniciamos la verificación
verificacion1PrimerCambio = verificarConPruebasT(primer_cambio,H0,"greater")
verificacion2PrimerCambio = verificarConPruebasT(primer_cambio,H0,"two-sided")

print("El valor 'p' para la hipotesis: primer cambio > 75 es ", verificacion1PrimerCambio.pvalue)
print("El valor 'p' para la hipotesis: primer cambio != 75 es ", verificacion2PrimerCambio.pvalue)


# Inicia la comparacion entre los datos para luego analizar la mejor solucion
comparacionInicialvsPrimerCambio = comparacionConPruebasT(primer_cambio, iniciales)
comparacionInicialvsSegundoCambio = comparacionConPruebasT(segundo_cambio, iniciales)
comparacionPrimerCambiovsSegundoCambio = comparacionConPruebasT(segundo_cambio, primer_cambio)

print("El valor 'p' para la hipotesis: Primer cambio > Inicial es ", comparacionInicialvsPrimerCambio.pvalue)
print("El valor 'p' para la hipotesis: Segundo cambio > Inicial es ", comparacionInicialvsSegundoCambio.pvalue)
print("El valor 'p' para la hipotesis: Segundo cambio > Primer cambio es ", comparacionPrimerCambiovsSegundoCambio.pvalue)
print("##########################################################################################")