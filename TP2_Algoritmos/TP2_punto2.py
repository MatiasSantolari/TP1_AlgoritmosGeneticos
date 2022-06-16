import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain, combinations
from collections import OrderedDict #lo uso para usar una funcion que ordene un diccionario por valor
import operator

# Definicion de variables globales
diccionarioObjetos = {'1' : [150, 20], '2' : [325, 40], '3': [600, 50], '4': [805, 36], '5': [430, 25], '6': [1200, 64], '7': [770, 54], '8': [60, 18], '9': [930, 46], '10': [353, 28]}
volumenMochila = 4200
diccionarioObjeto = {'1' : [150, 20], '2' : [325, 40], '3': [600, 50], '4': [805, 36], '5': [430, 25], '6': [1200, 64]}
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
        print(t)
        print(valor)
        print()
        dic [t] = valor
    print (dic)    
    return dic

def llenarMochila (listaOrdenada, diccionarioObjeto ):
    mochila = []
    volumenLibre = 1200
    conjunto = []
    for v in listaOrdenada:
        print("v:",v)
        obj = diccionarioObjeto.get(v[0])
        print("obj",obj)
        volumen = obj[0]
        if volumen < volumenLibre :
            print("el objeto ",v[0], " entra en la mochila")
            volumenLibre = volumenLibre - obj[0]
            print("el espacio libre que queda es ", volumenLibre)
            print()
            conjunto.append(v[0])
        else:
            print("No hay lugar")
            print()
    return conjunto

listaValores = {}
objetosMochila = []
listaObjetos = list(diccionarioObjeto.keys())
listaValores = busquedaHeuristica(listaObjetos, diccionarioObjeto)
listaOrdenada = sorted(listaValores.items(), key=operator.itemgetter(1), reverse=True)
print(listaOrdenada)
objetosMochila.extend(llenarMochila(listaOrdenada, diccionarioObjeto))
print("los objetos que entraron en la mochila son",objetosMochila)




