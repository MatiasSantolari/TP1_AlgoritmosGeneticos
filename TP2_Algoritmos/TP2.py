
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain, combinations

# Definicion de variables globales
diccionarioObjetos = {'1' : [150, 20], '2' : [325, 40], '3': [600, 50], '4': [805, 36], '5': [430, 25], '6': [1200, 64], '7': [770, 54], '8': [60, 18], '9': [930, 46], '10': [353, 28]}
volumenMochila = 4200
diccionarioObjeto = {'1' : [150, 20], '2' : [325, 40], '3': [600, 50], '4': [805, 36]}
"el diccionarioObjeto es para probar si se muestran todos los subconjuntos armador en generarSubConjuntos"

def generarSubConjuntos(list_name): #Esta funcion genera todos los subconjuntos de soluciones posibles que se pueden armar
    s = list(list_name)
    p = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return p # lo que retorna es una lista con todos los posibles subconjuntos que se pueden armar

def sumarVolumenes(solucion, diccionarioObjeto):
    total = 0
    for i in solucion:
        a = diccionarioObjeto.get(i)
        print (a[0])
        total = total + a [0]
    #print ("el total es: ", total)
    return total

def validarRestriccion(volumenTotal):
    if volumenTotal <= 1200:
        return True
    else:
        return False

listaObjetos = list(diccionarioObjeto.keys())
for i in listaObjetos:
    print (i)

print("Los subconjuntos posibles a armar son:")
soluciones = generarSubConjuntos(listaObjetos)
listaSolucionesValidas = []
for x in soluciones:
     print(x)
     volumenTotal = sumarVolumenes(x, diccionarioObjeto)
     print("la suma de todos los volumenes de esta solucion es: ", volumenTotal)
     valido = validarRestriccion(volumenTotal)
     if valido:
         listaSolucionesValidas.append(x)
print("Las soluciones que cumplen la restriccion son: ")
for i in listaSolucionesValidas:
    print(i)
