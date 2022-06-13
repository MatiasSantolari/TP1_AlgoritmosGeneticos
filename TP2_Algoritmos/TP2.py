
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
    lista = list(p)
    # print (lista)
    for x in lista:
        #print(x)
        if len(x) == 0: #saco de la lista la solucion vacia 
            lista.remove(x)
    #print (lista)
    p = tuple(lista)        
    return p # lo que retorna son tuplas que representan todos los posibles subconjuntos que se pueden armar

def sumarVolumenes(solucion, diccionarioObjeto):
    total = 0
    for i in solucion:
        a = diccionarioObjeto.get(i)
        print (a[0])
        total = total + a [0]
    #print ("el total es: ", total)
    return total

def verificarRestriccion(volumenTotal):
    if volumenTotal <= 1200: # ACA VA 4200 POR EL VOLUMEN DE LA MOCHILA
        return True
    else:
        return False

def calcularValor(solucionValida,diccionarioObjeto):
    valorTotal = 0
    for l in solucionValida:
        b = diccionarioObjeto.get(l)
        print("valor: ",b[1])
        valorTotal = valorTotal + b[1]
    print("el valor total del subconjunto es: ", valorTotal)
    return valorTotal

listaObjetos = list(diccionarioObjeto.keys()) #genero una lista con las claves de cada objero
for i in listaObjetos:
    print (i)

print("Los subconjuntos posibles a armar son:")
soluciones = generarSubConjuntos(listaObjetos) # soluciones es una tupla con todos los subconjuntos posibles de todos los indices de los objetos
listaSolucionesValidas = []
listaValoresSoluciones = []
valorMaximo = 0
print("las soluciones posibles formadas por los numeros de los objetos son: ", soluciones)
print()
for x in soluciones:
     print(x)
     volumenTotal = sumarVolumenes(x, diccionarioObjeto)
     print("la suma de todos los volumenes de esta solucion es: ", volumenTotal)
     valido = verificarRestriccion(volumenTotal)
     if valido:
         listaSolucionesValidas.append(x)
print("Las soluciones que cumplen la restriccion son: ", listaSolucionesValidas)
for i in listaSolucionesValidas:
    print(i)
    v = calcularValor(i,diccionarioObjeto)
    listaValoresSoluciones.append(v)
    if (v > valorMaximo):
        valorMaximo = v
        solucionMaxima = i
print (listaValoresSoluciones)
# valorMaximo = max(listaValoresSoluciones)
print("el valor mas alto es: ", valorMaximo, "correspondiente a la solucion: ", solucionMaxima)