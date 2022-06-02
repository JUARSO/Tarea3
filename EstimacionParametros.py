import numpy
import pandas
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
from sympy import re

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