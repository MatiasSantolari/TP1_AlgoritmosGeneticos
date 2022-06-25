#TP 2 punto 3
from itertools import chain, combinations

diccionarioObjeto = {'1' : [1800, 72], '2' : [600, 36], '3': [1200, 60]} #en la posicion 0 esta el peso y en la posicion 1 esta el valor

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

def sumarPesos(solucion, diccionarioObjeto):
    total = 0
    for i in solucion:
        a = diccionarioObjeto.get(i)
        print (a[0])
        total = total + a [0]
    return total