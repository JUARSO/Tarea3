import numpy
import pandas
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

datosExcel = pandas.read_excel("Tarea3\Conjunto_datos_tarea2.xlsx")



#Se separan en diferentes listas las muestras utilizadas
muestraInicial = datosExcel['Inicial']
muestraPrimerCambio=datosExcel["Primer_cambio"]
muestraSegundoCambio=datosExcel["Segundo_cambio"]

#se calcula la media para la muestra incial, muestra con el Primer Cambio y Muestras con el segundo cambio 
mediaIncial = muestraInicial.mean()
mediaCambio1 = muestraPrimerCambio.mean()
mediaCambio2 = muestraSegundoCambio.mean()

#Calculo de las desviaciones estandar para la muestra incial, muestra con el Primer Cambio y Muestras con el segundo cambio 
desviacionEstandarInciail = muestraInicial.std()
desviacionEstandarCambio1 = muestraPrimerCambio.std()
desviacionEstandarCambio2 = muestraSegundoCambio.std()



#se calcula la desviacion estadar de las muestra inical, la muestra del primer cambio y la muestras del segundo cambio con MLE usando la media conocida
desviacionEstandarInciailMLE= stats.norm.fit(muestraInicial,floc=mediaIncial)[1]
desviacionEstandarCambio1MLE= stats.norm.fit(muestraPrimerCambio,floc=mediaCambio1)[1]
desviacionEstandarCambio2MLE= stats.norm.fit(muestraSegundoCambio,floc=mediaCambio2)[1]

print("media inicial: ", mediaIncial)
print("desviacion estandar inicial: ", desviacionEstandarInciail)
print("desviacion estandar inicial MLE: ", desviacionEstandarInciailMLE)
print("varianza inicial: ", math.pow(desviacionEstandarInciail,2))
print("varianza inicial MLE: ", math.pow(desviacionEstandarInciailMLE,2))
print("---------------------------------------------------------------------------------------------------------")

print("media primer cambio: ", mediaCambio1)
print("desviacion estandar primer cambio: ", desviacionEstandarCambio1)
print("desviacion estandar primer cambio MLE: ", desviacionEstandarCambio1MLE)
print("varianza primer cambio: ", math.pow(desviacionEstandarCambio1,2))
print("varianza primer cambio MLE: ", math.pow(desviacionEstandarCambio1MLE,2))
print("---------------------------------------------------------------------------------------------------------")

print("media segundo cambio: ", mediaCambio2)
print("desviacion estandar segundo cambio: ", desviacionEstandarCambio2)
print("desviacion estandar segundo cambio MLE: ", desviacionEstandarCambio2MLE)
print("varianza segundo cambio: ", math.pow(desviacionEstandarCambio2,2))
print("varianza segundo cambio MLE: ", math.pow(desviacionEstandarCambio2MLE,2))
print("---------------------------------------------------------------------------------------------------------")