import random
import pandas as pd
import numpy as np

# definicion de variables globales
probabilidadCrossover = 0.75
probabilidadMutacion = 0.05

# funcion que crea un cromosoma de 30 genes, donde cada gen es un dígito binario 0 o 1
def definirCromosoma():
    cromosoma= ""
    num=0
    for i in range(30):
        num = str(random.randint(0,1)) # 
        cromosoma += num
    return cromosoma

    
 # funcion objetivo f(x) donde x es el número entero del cromosoma que se pasa como parámetro
def funcionObjetivo(x:int):    
    coef = (2**30)-1
    funcObj= (x / coef)**2
    return funcObj 

def fitness(x,subLista) -> float: 
    return x/sum(subLista)

# funcion para seleccionar un cromosoma aleatoriamente de la poblacion inicial
def seleccionCromosoma(numero):
    return random.choice(numero)

def binarioAdecimal(subLista):
    listaDec=[]    
    for i in range(len(subLista)):
        cr = str(subLista[i])
        a = int(cr,2)
        listaDec.append(a)
    return listaDec
    
def aplicarFunObj(subLista):
    listaF=[]
    for m in range(len(subLista)):
        
        f=funcionObjetivo(int(subLista[m]))
        listaF.append(f)
    return listaF
    
def aplicarFitness(subLista):
    listaFit=[]
    for m in subLista:
        f=fitness(m,subLista)
        listaFit.append(f)
    return listaFit # retorna una lista de flotantes

def suma(listaFunObj): #suma todos los valores de la funcion objetivo de cada cromosoma
    cont=0    
    for u in range(len(listaFunObj)):
        cont+= listaFunObj[u]
    return cont

def promedio(listaFunObj): #calcula el promedio 
    suma=0    
    for u in range(len(listaFunObj)):
        suma= listaFunObj[u]
    resultado = suma / len(listaFunObj)
    return resultado

def maximo(listaFunObj): #devuelve el valor maximo de la lista funcion objetivo
    return max(listaFunObj)

#-----------------------------------------------------------------------------------------------------------
#En esta seccion se van a ver las funciones o lo relacionado con la seleccion, crossover y mutacion

def partRuleta(listaFitness): # se calcula el porcentaje de cada cromosoma y se le asigna
                               #un arco de circunferencia proporcional a su fitness. porc 
    i = 0
    listaPorcentajeFitness=[]
    for b in range(len(listaFitness)):
        den = sum(listaFitness)
        nu = round((listaFitness[i]/den) * 100,2)
        listaPorcentajeFitness.append(nu)
        i+=1     
    return listaPorcentajeFitness

def seleccionRuleta():
    return

def seleccionCrossover():
    return

def seleccionMutacion():
    return

    
#Aca inicia el main del TP 
i=0
poblacion =[]   
lista=[]
listaPoblacionInicial=[]
listaDecimales=[]
listaFunObj=[]
listaFitness=[]
for j in range(10):
    cromo = definirCromosoma()
    num = int(cromo)
    lista.append(num)
print (lista)
print ()
for k in range(4):
    listaPoblacionInicial.append(seleccionCromosoma(lista))
print("Los cromosomas seleccionados son " ,listaPoblacionInicial) #contiene los cromosomas seleccionados
print()
listaDecimales.extend(binarioAdecimal(listaPoblacionInicial))
print("Los numeros decimales de cada cromosoma correspondiente son " ,listaDecimales)
print()
listaFunObj.extend(aplicarFunObj(listaDecimales))
print("valor de la funcion objetivo de cada cromosoma:",listaFunObj)
print()
listaFitness.extend(aplicarFitness(listaFunObj))
print("fitness",listaFitness)
print()
print("la suma de todos los valores de la funcion objetivo es: ", suma(listaFunObj))
print()
print(partRuleta(listaFitness))


#p=0
#print("Binario                                   X          Funcion Objetivo               Fitness")
#print()
#for l in range(4):
#    print(listaPoblacionInicial[p], "     ",listaDecimales[p],"        ",listaFunObj[p],"        ",listaFitness[p])
#    p+=1

