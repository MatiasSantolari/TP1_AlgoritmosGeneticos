'''import random

lista1=['a','b','c','d','e','f','g','h','i','j']
lista2=[1,2,3,4,5,6,7,8,9,10]
aux=[]
a=random.randint(0,9)
print (a)
for j in range(a):
    print(j)
    aux.append(lista1[j])
for i in range(a,len(lista1)):
    print(i)
    aux.append(lista2[i])
    lista2[i] = lista1[i]
print (lista1)
print()
print (lista2)
print (aux)'''

'''
cromosoma = ""
    num = 0
    for i in range(30):
        num = str(random.randint(0, 1))  #
        cromosoma += num
    return cromosoma
    '''

'''
nuevaG=[[1,0,1,0],[0,1,0,0],[0,0,1,1]]
listaPrueba=["jasjdjajsdjas", 2222 , [1,2,3,4]]
listaCorrectaCadena=[]
listaCorrectaNro=[]


for i in range(len(nuevaG)):
    print()
    a = ""
    for j in nuevaG[i]:
        a += str(j)
    listaCorrectaCadena.append(a)
    listaCorrectaNro.append(int(a))

print(listaCorrectaCadena)
print(listaCorrectaNro)
listaPrueba=listaCorrectaCadena
print(listaPrueba)
'''

'''
import random
import pandas as pd

listaPrueba=[]
for i in range(4):
    a=random.randint(1,10)
    b=random.randint(1,1000)
    c=random.randint(1,5)

    listaPrueba.append([a,b,c])

print (listaPrueba)

#--------------
listaA=[]
listaB=[]
listaC=[]
print('Datos Globales')
for i in range (len(listaPrueba)):
    a=listaPrueba[i][0]
    b=listaPrueba[i][1]
    c=listaPrueba[i][2]

    listaA.append(a)
    listaB.append(b)
    listaC.append(c)

tabla = pd.DataFrame({'min': listaA, 'max': listaB, 'promedio': listaC})
print(tabla)

'''

from random import randint
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

listamin=[1,2,3,4,5]
listamax=[1,3,6,9,8]
listaprob=[2,3,6,9,8]

tablaMinFit = pd.DataFrame({'Min Fitness': listamin})
print(tablaMinFit)
tablaMaxFit = pd.DataFrame({'Max Fitness': listamax})
print(tablaMaxFit)
tablaProbFit = pd.DataFrame({'Probabilidad Fitness': listaprob})
print(tablaProbFit)

plt.style.use('default')
plt.plot(tablaMinFit, label='Min Fitness')
plt.plot(tablaMaxFit, label='Max Fitness')
plt.plot(tablaProbFit, label='Probabilidad Fitness')
plt.legend()
plt.title('Fitness')
plt.xlabel('generaciones')
plt.grid(True)
plt.show()










