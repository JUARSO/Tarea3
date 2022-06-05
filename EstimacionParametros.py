import pandas
import scipy.stats as stats
import matplotlib.pyplot as plt
import math


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