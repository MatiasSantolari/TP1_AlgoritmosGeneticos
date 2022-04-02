import random
import matplotlib.pyplot as plt
import numpy as np


def definirCromosoma():
    cromosoma= []
    for i in range(30):
        cromosoma.append(random.randint(0,1))
    return cromosoma

def crearpoblacion():
    poblacion = []
    for j in range(10):
        c = definirCromosoma
        poblacion.append(c)

