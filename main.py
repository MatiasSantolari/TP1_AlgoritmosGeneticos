import numpy as np
import matplotlib.pyplot as plt
import openpyxl as xl
import pandas as pd
import random
import math

N=10  #Tamaño de la poblacion inicial
Gmax=20  # Número máximo de iteraciones
all_max=0   #El valor óptimo
pm=0.05
pc=0.75

def poblacionEntera():
    poblacion = []
    #for i in range((2**6)):
        #poblacion.append(i)
    poblacion.extend(range(2**30))
    return poblacion

def crearPoblacionInicial():
    poblacion = []
    todoElPueblo = poblacionEntera()
    print(todoElPueblo)
    for i in range(10):
        poblacion.append(bin(random.randint(todoElPueblo[0],todoElPueblo[len(todoElPueblo)-1])))
    return poblacion


poblado=[]
poblado=crearPoblacionInicial()
for i in poblado:
    print(i)

print (poblado)
