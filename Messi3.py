from tkinter import E
from urllib.request import CacheFTPHandler
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

RutaArchivo = 'C:/Users/Asus/Downloads/Tarea3/Tarea3.xlsx'
Archivo = pd.read_excel(RutaArchivo)
#print(Archivo)

Muestra_Inicial =       Archivo[['Inicial']]
Muestra_PrimerCambio=   Archivo[['Primer_cambio']]
Muestra_SegundoCambio=  Archivo[['Segundo_cambio']]

#Fución para el cálculo para las medias de las muestras
def medias_Muestras(muestra):
    Muestra= muestra.mean()
    return Muestra


#  Asignacion  de las medias a una varible 
A = medias_Muestras(Muestra_Inicial)
B = medias_Muestras(Muestra_PrimerCambio)
C = medias_Muestras(Muestra_SegundoCambio)


# Medias de las muestras
Media_MuestraInicial='La media de la Muestra Inicial es:  ',        A
Media_PrimerCambio = 'La media de la Muestra del Primer cambio: ',  B
Media_SegundoCambio= 'La media de la Muestra del Segundo Cambio: ', C

# Calculo para la desviación estándar para las muestras

def DesviacionStandar_Muestras(muestra):
    Muestra= muestra.std()
    return Muestra


#  Asignacion  de las desviaciones estandares a una varible 
D = DesviacionStandar_Muestras(Muestra_Inicial)
E = DesviacionStandar_Muestras(Muestra_PrimerCambio)
F = DesviacionStandar_Muestras(Muestra_SegundoCambio)

# Medias de las muestras
Std_MuestraInicial='La desviación estándar de la Muestra Inicial es:  ',        D
Std_PrimerCambio = 'La desviación estándar de la Muestra del Primer cambio: ',  E
Std_SegundoCambio= 'La desviación estándar de la Muestra del Segundo Cambio: ', F

#Creación de la grafica correpondiente, utilizando la función de desidad de probabilidad calculada en X, la cual la llamaremos "Fdp"

#def Histograma(Muestra,Media,Std,N, Verosimilitud):
    #Muestra = sorted(Muestra)
    #figura = plt.subplot(sharex ='all', sharey='all').twinx()
    #dimenciones = stats.norm.pdf(Muestra,Media,Std)
    #dimenciones_Verosimilitud= stats.norm.pdf(Muestra, Media, Verosimilitud)
    #Primera_Linea= figura.plot(Muestra, dimenciones,'K')
    #Segunda_Linea =figura.plot(Muestra,dimenciones_Verosimilitud,'K')
    #Figura1_2=plt.subplot(sharex ='all', sharey='all')
    #Figura1_2.hist(Muestra,bins=range(len(Muestra)),color= 'green')
    #Figura1_2.set_xlabel("Redemiento de los datos de las muestras")
    #figura.set_ylabel('Función de desidad de Probabilidad (Fdp)')
    #plt.tittle('Función de Maxima Verosimitud (MLE) de', N)

def crear_grafica(muestra,deMLE2,de,media, nombre):
    muestra=sorted(muestra) # definida en la función
    p1=plt.subplots(sharex='all')
    p2=p1.twinx()
    fit = stats.norm.pdf(muestra,media,de)
    fit_MLE=stats.norm.pdf(muestra,media,deMLE2)
    l1,=p2.plot(muestra, fit,'-r')
    l2,=p2.plot(muestra,fit_MLE,'-g')
    l1.set_label('analitica')
    l2.set_label('MLE')
    p2.legend()
    p1.hist(muestra,edgecolor="black")
    p2.set_ylabel("PDF")
    p1.set_ylabel("Frecuencia de los datos")
    plt.title("Histograma de Frecuencia,pdf de: "+ nombre)
    p1.set_xlabel("porcentaje de rendimiento")
    plt.show()

deMLE2= stats.norm.fit(Muestra_Inicial,floc=A)[1]
crear_grafica(Muestra_Inicial,deMLE2,D,A,"Inicial")

#Verosimilitud2= stats.norm.fit(Muestra_Inicial,floc=D)[1]
#crear_grafica(Muestra_Inicial,A,D,'Inicial', Verosimilitud2)




#plt.hist(campo, bins=range(len(Archivo)), orientation='vertical')#bins=range(len(campo)), align='left', orientation='vertical', color= 'green
#plt.title('Tabala 2: Función de masa de probabilidad (Binomial Negativa)')#Crea el titulo principla
#plt.xlabel('X') # subtitulo para el eje X
#plt.ylabel('F(x)')#Subtitulo para el eje y
#plt.show()#imprime los resultados en la pantalla
