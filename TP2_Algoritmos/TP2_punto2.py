#TP 2 punto 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain, combinations
from collections import OrderedDict #lo uso para usar una funcion que ordene un diccionario por valor
import operator

# Definicion de variables globales
diccionarioObjetos = {'1' : [150, 20], '2' : [325, 40], '3': [600, 50], '4': [805, 36], '5': [430, 25], '6': [1200, 64], '7': [770, 54], '8': [60, 18], '9': [930, 46], '10': [353, 28]}
volumenMochila = 4200
diccionarioObjeto = {'1' : [150, 20], '2' : [325, 40], '3': [600, 50], '4': [805, 36], '5': [430, 25], '6': [1200, 64], '7': [770, 54], '8': [60, 18], '9': [930, 46], '10': [353, 28]}
"el diccionarioObjeto es para probar si se muestran todos los subconjuntos armador en generarSubConjuntos"


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
        print("objeto: ",t)
        print("valor / volumen =", num,"/",den,"=", valor)
        print()
        dic [t] = valor
    print("Objetos con su respectivo resultado:")
    print (dic)    
    return dic

def llenarMochila (listaOrdenada, diccionarioObjeto ):
    mochila = []
    volumenLibre = 4200
    conjunto = []
    for v in listaOrdenada:
        print("Objeto ",v[0])
        obj = diccionarioObjeto.get(v[0])
        print("volumen:",obj[0], "cm3")
        volumen = obj[0]
        if volumen < volumenLibre :
            print("el objeto ",v[0], " entra en la mochila")
            print(volumenLibre, "-", obj[0]," cm3")
            volumenLibre = volumenLibre - obj[0]
            print("el espacio libre que queda es ", volumenLibre,"cm3")
            print()
            conjunto.append(v[0])
        else:
            print("No hay lugar")
            print()
    return conjunto

volTotal = 0
listaValores = {}
objetosMochila = []
listaObjetos = list(diccionarioObjeto.keys())
listaValores = busquedaHeuristica(listaObjetos, diccionarioObjeto)
listaOrdenada = sorted(listaValores.items(), key=operator.itemgetter(1), reverse=True)
print()
print("Lista de objetos ordenada de mayor a menor segun resultado calculado anteriormente:")
print(listaOrdenada)
print()
objetosMochila.extend(llenarMochila(listaOrdenada, diccionarioObjeto))
for o in objetosMochila:
    vol= diccionarioObjeto.get(o)
    # print(vol)
    volTotal= volTotal + vol[0]
print("los objetos que entraron en la mochila son",objetosMochila, "con un volumen en total de:",volTotal,"cm3")




