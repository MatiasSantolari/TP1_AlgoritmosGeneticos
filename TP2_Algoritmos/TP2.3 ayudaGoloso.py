#TP2 punto 3 metodoGoloso
from collections import OrderedDict #lo uso para usar una funcion que ordene un diccionario por valor
import operator

# Definicion de variables globales
diccionarioObjeto = {'1' : [1800, 72], '2' : [600, 36], '3': [1200, 60]} #en la posicion 0 esta el peso y en la posicion 1 esta el valor

#se hace 10 divisiones, una por cada objeto, donde la division es valor / volumen
def busquedaHeuristica(lista, diccionarioObjeto): 
    listaV = []
    dic ={}
    for t in lista:
        li = diccionarioObjeto.get(t)
        num = li[1]
        den = li[0]
        valor = num / den
        listaV.append(valor)
        print("Objeto: ",t)
        print("valor / volumen =", num,"/",den,"=", valor)
        print()
        dic [t] = valor
    print("Objetos con su respectivo resultado:")
    print (dic)    
    return dic

def llenarMochila (listaOrdenada, diccionarioObjeto ):
    mochila = []
    pesoLibre = 3000
    conjunto = []
    for v in listaOrdenada:
        print("Objeto ",v[0])
        obj = diccionarioObjeto.get(v[0])
        print("peso:",obj[0], "grs")
        peso = obj[0]
        if peso < pesoLibre :
            print("el objeto ",v[0], " entra en la mochila")
            print(pesoLibre, "-", obj[0],"grs")
            pesoLibre = pesoLibre - obj[0]
            print("el peso libre que queda es ", pesoLibre,"grs")
            print()
            conjunto.append(v[0])
        else:
            print("No hay peso suficiente para soportar el objeto")
            print()
    return conjunto

pesoTotal = 0
listaValores = {}
objetosMochila = []
listaObjetos = list(diccionarioObjeto.keys())
listaValores = busquedaHeuristica(listaObjetos, diccionarioObjeto)
print()
listaOrdenada = sorted(listaValores.items(), key=operator.itemgetter(1), reverse=True)
print("Lista de objetos ordenadas")
print(listaOrdenada)
print()
objetosMochila.extend(llenarMochila(listaOrdenada, diccionarioObjeto))
for o in objetosMochila:
    pes= diccionarioObjeto.get(o)
    #print(pes)
    pesoTotal= pesoTotal + pes[0]
print("los objetos que entraron en la mochila son",objetosMochila, "con un peso en total de:",pesoTotal,"grs")
