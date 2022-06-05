import pandas
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

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


datosExcel = pandas.read_excel("Tarea3\Conjunto_datos_tarea2.xlsx")

#Se separan en diferentes listas las muestras utilizadas
def extracion_de_datos():
    muestraInicial = datosExcel['Inicial']
    muestraPrimerCambio=datosExcel["Primer_cambio"]
    muestraSegundoCambio=datosExcel["Segundo_cambio"]
    return (muestraInicial, muestraPrimerCambio, muestraSegundoCambio)

#se calcula la media para la muestra incial, muestra con el Primer Cambio y Muestras con el segundo cambio 
def calculo_de_medias():
    mediaIncial = extracion_de_datos()[0].mean()
    mediaCambio1 = extracion_de_datos()[1].mean()
    mediaCambio2 = extracion_de_datos()[2].mean()
    return (mediaIncial, mediaCambio1, mediaCambio2)

#Calculo de las desviaciones estandar para la muestra incial, muestra con el Primer Cambio y Muestras con el segundo cambio 
def calculo_de_desviaciones():
    desviacionEstandarInciail = extracion_de_datos()[0].std()
    desviacionEstandarCambio1 = extracion_de_datos()[1].std()
    desviacionEstandarCambio2 = extracion_de_datos()[2].std()
    return (desviacionEstandarInciail, desviacionEstandarCambio1 , desviacionEstandarCambio2)

#se calcula la desviacion estadar de las muestra inical, la muestra del primer cambio y la muestras del segundo cambio con MLE usando la media conocida
def calculo_desviacion_con_MLE():
    desviacionEstandarInciailMLE= stats.norm.fit(extracion_de_datos()[0],floc=calculo_de_medias()[0])[1]
    desviacionEstandarCambio1MLE= stats.norm.fit(extracion_de_datos()[1],floc=calculo_de_medias()[1])[1]
    desviacionEstandarCambio2MLE= stats.norm.fit(extracion_de_datos()[2],floc=calculo_de_medias()[2])[1]
    return (desviacionEstandarInciailMLE, desviacionEstandarCambio1MLE, desviacionEstandarCambio2MLE)

print("media inicial: ", calculo_de_medias()[0])
print("desviacion estandar inicial: ", calculo_de_desviaciones()[0])
print("desviacion estandar inicial MLE: ", calculo_desviacion_con_MLE()[0])
print("varianza inicial: ", math.pow(calculo_de_desviaciones()[0],2))
print("varianza inicial MLE: ", math.pow(calculo_desviacion_con_MLE()[0],2))
print("#########################################################################################################")

print("media primer cambio: ", calculo_de_medias()[1])
print("desviacion estandar primer cambio: ", calculo_de_desviaciones()[1])
print("desviacion estandar primer cambio MLE: ", calculo_desviacion_con_MLE()[1])
print("varianza primer cambio: ", math.pow(calculo_de_desviaciones()[1],2))
print("varianza primer cambio MLE: ",math.pow(calculo_desviacion_con_MLE()[1],2))
print("#########################################################################################################")

print("media segundo cambio: ", calculo_de_medias()[2])
print("desviacion estandar segundo cambio: ",calculo_de_desviaciones()[2])
print("desviacion estandar segundo cambio MLE: ", calculo_desviacion_con_MLE()[2])
print("varianza segundo cambio: ", math.pow(calculo_de_desviaciones()[2],2))
print("varianza segundo cambio MLE: ", math.pow(calculo_desviacion_con_MLE()[2],2))
print("#########################################################################################################")


def crear_grafica(muestra,mle,de,media, nombre):
    muestra=sorted(muestra)
    f,p1=plt.subplots(sharex='all')
    p2=p1.twinx()
    fit = stats.norm.pdf(muestra,media,de)
    fit_MLE=stats.norm.pdf(muestra,media,mle)
    l1,=p2.plot(muestra, fit, '-r')
    l2,=p2.plot(muestra,fit_MLE,'-g')
    l1.set_label('analitica')
    l2.set_label('MLE')
    p2.legend()
    p1.hist(muestra,edgecolor="black")
    p2.set_ylabel("PDF")
    p1.set_ylabel("Frecuencia de los datos")
    plt.title("Histograma de Frecuencia "+ nombre)
    p1.set_xlabel("Rendimiento")
    plt.show()

#crear_grafica(extracion_de_datos()[0],calculo_desviacion_con_MLE()[0],calculo_de_desviaciones()[0],calculo_de_medias()[0],"Inicial")
#crear_grafica(extracion_de_datos()[1],calculo_desviacion_con_MLE()[1],calculo_de_desviaciones()[1],calculo_de_medias()[1],"Primer Cambio")
#crear_grafica(extracion_de_datos()[0],calculo_desviacion_con_MLE()[0],calculo_de_desviaciones()[0],calculo_de_medias()[0],"Segundo Cambio")


def crear_grafica_juan(muestra, nombre):
    muestra=sorted(muestra)
    f,p1=plt.subplots(sharex='all', sharey='all')
    p2=p1.twinx()
    p2.legend()
    p1.hist(muestra,color= 'grey')
    p1.set_ylabel("Frecuencia de los datos")
    plt.title("Histograma de la densidad de probabilidad para "+ nombre)
    p1.set_xlabel("Redemiento de los datos de las muestras")
    plt.show()

def normal_Estandar(muestra, media, Std,N):
    muestra=sorted(muestra)
    fdP_normal = stats.norm.pdf(muestra,media,Std) # FDP
    plt.plot(muestra, fdP_normal,'k', label='FDP nomal')
    plt.title('Función de Densidad de Probabilidad  '+ N)
    plt.ylabel('probabilidad')
    plt.xlabel('valores')
    plt.show()

normal_Estandar(extracion_de_datos()[0], extracion_de_datos()[0].mean(), extracion_de_datos()[0].std(),"Inicial")
normal_Estandar(extracion_de_datos()[1], extracion_de_datos()[1].mean(), extracion_de_datos()[1].std(),"Primer Cambio")
normal_Estandar(extracion_de_datos()[2], extracion_de_datos()[2].mean(), extracion_de_datos()[2].std(),"Segundo Cambio")


crear_grafica_juan(extracion_de_datos()[0],"Inicial")
crear_grafica_juan(extracion_de_datos()[1],"Primer Cambio")
crear_grafica_juan(extracion_de_datos()[0],"Segundo Cambio")