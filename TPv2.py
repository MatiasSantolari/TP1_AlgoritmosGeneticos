import random
import pandas as pd
import numpy as np

# definicion de variables globales
probabilidadCrossover = 0.75
probabilidadMutacion = 0.05


# funcion que crea un cromosoma de 30 genes, donde cada gen es un dígito binario 0 o 1
def definirCromosoma():
    cromosoma = ""
    num = 0
    for i in range(30):
        num = str(random.randint(0, 1))  #
        cromosoma += num
    return cromosoma


# funcion objetivo f(x) donde x es el número entero del cromosoma que se pasa como parámetro
def funcionObjetivo(x: int):
    coef = (2 ** 30) - 1
    funcObj = (x / coef) ** 2
    return funcObj


def fitness(x, subLista) -> float:
    return x / sum(subLista)


def binarioAdecimal(subLista):
    listaDec = []
    for i in range(len(subLista)):
        cr = str(subLista[i])
        a = int(cr, 2)
        listaDec.append(a)
    return listaDec


def aplicarFunObj(subLista):
    listaF = []
    for m in range(len(subLista)):
        f = funcionObjetivo(int(subLista[m]))
        listaF.append(f)
    return listaF


def aplicarFitness(subLista):
    listaFit = []
    for m in subLista:
        f = fitness(m, subLista)
        listaFit.append(f)
    return listaFit  # retorna una lista de flotantes


def suma(listaFunObj):  # suma todos los valores de la funcion objetivo de cada cromosoma
    cont = 0
    for u in range(len(listaFunObj)):
        cont += listaFunObj[u]
    return cont


def promedio(listaFunObj):  # calcula el promedio
    suma = 0
    for u in range(len(listaFunObj)):
        suma = listaFunObj[u]
    resultado = suma / len(listaFunObj)
    return resultado


def maximo(listaFunObj):  # devuelve el valor maximo de la lista funcion objetivo
    return max(listaFunObj)


# -----------------------------------------------------------------------------------------------------------
# En esta seccion se van a ver las funciones o lo relacionado con la seleccion, crossover y mutacion

def partRuleta(listaFitness):  # se calcula el porcentaje de cada cromosoma y se le asigna
    # un arco de circunferencia proporcional a su fitness. porc
    i = 0
    listaPorcentajeFitness = []
    for b in range(len(listaFitness)):
        den = sum(listaFitness)
        nu = round((listaFitness[i] / den) * 100, 2)
        listaPorcentajeFitness.append(nu)
        i += 1
    return listaPorcentajeFitness

'''
def seleccionRuleta(ruleta, posiciones, poblacion): #posiciones es int(sum(ruleta)) 
    #dict_from_list = dict(zip(list(range(10)), poblacion))
    padres={} #definicion de la tupla padres
    poscRuleta=[] #definicion de la list poscRuleta
    for j in range(10):
        a = random.randint(0, posiciones)
        n=0
        for i in ruleta:
            n+=i
            if a<=n:
                poscRuleta.append(i)
                padres[j]=i
                break
    # print('dale que saleeeeeee')
    print(poscRuleta)
    print(padres)
    #print(dict_from_list)'''

def seleccionRuleta(ruleta, posiciones, poblacion): #posiciones es int(sum(ruleta))
    ruletaDefinitiva=[]
    padres=[]
    for i in range(10):
        for j in range(ruleta[i]):
            ruletaDefinitiva.append(poblacion[i])
    for k in range(10):
        a = random.randint(0, posiciones)
        padres.append(ruletaDefinitiva[a])
    return padres

def seleccionCrossover(padres):
    # para pasar de un numero entero a una lista de enteros
    '''num = 1010
    print (str(num))
    lis = list(map(int,str(num)))
    print(lis)'''
    
    # hago la lista de par de padres
    '''n=0
    lista=[]
    for i in range(5):
        lista.append([n,n+1])
        n+=2
        print(lista)'''
    
    for i in range(5):
        for j in padres:
        a = random.randint(0, 1)
        if (a <= probabilidadCrossover):
            pass
        else:
            listaHijos.append()
        
    return


def seleccionMutacion():
    return


# Aca inicia el main del TP
i = 0
poblacion = []
lista = []
listaPoblacionInicial = []
listaDecimales = []
listaFunObj = []
listaFitness = []
listaPadres = []
listaHijos = []
for j in range(10):
    cromo = definirCromosoma()
    num = int(cromo)
    listaPoblacionInicial.append(num)
print("Los cromosomas seleccionados son ", listaPoblacionInicial)  # contiene los cromosomas
listaPoblacionInicial.sort()
print()
print()
listaDecimales.extend(binarioAdecimal(listaPoblacionInicial))
print("Los numeros decimales de cada cromosoma correspondiente son ", listaDecimales)
print()
listaFunObj.extend(aplicarFunObj(listaDecimales))
print("valor de la funcion objetivo de cada cromosoma:", listaFunObj)
print()
listaFitness.extend(aplicarFitness(listaFunObj))
print("fitness", listaFitness)
print()
print("la suma de todos los valores de la funcion objetivo es: ", suma(listaFunObj))
print()

tabla = pd.DataFrame(
    {'pobl': listaPoblacionInicial, 'X': listaDecimales, 'F obj': listaFunObj, 'Fitness': listaFitness})
print(tabla)

print()
print('los porcentajes de cada cromosoma dependiendo de su funcion fitnes es', partRuleta(listaFitness))
print()

ruleta = []
for i in partRuleta(listaFitness):
    if i > 1:
        n = round(i, 0)
        ruleta.append(int(n))
    else:
        ruleta.append(1)

print('redondeo de los procentajes de cada cromosoma dependiendo de su funcion fitnes y que no haya perocentajes menores a 1:', ruleta)
print()
print('comprobacion que la suma de los porcentajes da 100:',int(sum(ruleta)))
print()
listaPadres.extend(seleccionRuleta(ruleta, int(sum(ruleta)), listaPoblacionInicial))
print('La lista de los padres es: ',listaPadres)

