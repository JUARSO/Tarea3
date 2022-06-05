import pandas
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
import parte_2

def histogramasNormalEstandar(muestra, media , Std, nombre):
    muestra=sorted(muestra)
    f,p1=plt.subplots(sharex='all', sharey='all')
    p2=p1.twinx()
    fdP_normal = stats.norm.pdf(muestra,media,Std) # FDP
    p2.plot(muestra, fdP_normal, 'black')
    p2.legend()
    p1.hist(muestra,color= 'grey')
    p1.set_ylabel("Frecuencia de los datos")
    plt.title("Histograma de la densidad de probabilidad para "+ nombre)
    p1.set_xlabel("Redemiento de los datos de las muestras")
    plt.show()



histogramasNormalEstandar(parte_2.extracion_de_datos()[0], parte_2.calculo_de_medias()[0], parte_2.calculo_desviacion_con_MLE()[0],"Inicial")
histogramasNormalEstandar(parte_2.extracion_de_datos()[1], parte_2.calculo_de_medias()[1], parte_2.calculo_desviacion_con_MLE()[1],"Primer Cambio")
histogramasNormalEstandar(parte_2.extracion_de_datos()[2], parte_2.calculo_de_medias()[2], parte_2.calculo_desviacion_con_MLE()[2],"Segundo Cambio")

