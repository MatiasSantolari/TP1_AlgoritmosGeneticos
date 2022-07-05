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
        #print (a[0])
        total = total + a [0]
    return total

def verificarRestriccion(pesoTotal):
    if pesoTotal <= 3000: 
        return True
    else:
        return False

def calcularValor(solucionValida,diccionarioObjeto):
    valorTotal = 0
    for l in solucionValida:
        b = diccionarioObjeto.get(l)
        # print("valor: ",b[1])
        valorTotal = valorTotal + b[1]
    print("el valor total del subconjunto es: $", valorTotal)
    return valorTotal

print(diccionarioObjeto)
print()
listaObjetos = list(diccionarioObjeto.keys()) #genero una lista con las claves de cada objero
#print("Los subconjuntos posibles a armar son:")
soluciones = generarSubConjuntos(listaObjetos) # soluciones es una tupla con todos los subconjuntos posibles de todos los indices de los objetos
listaSolucionesValidas = []
listaValoresSoluciones = []
valorMaximo = 0
print("las soluciones posibles formadas por los numeros de los objetos son: ", soluciones)
print()
for x in soluciones:
     print("Solucion:", x)
     pesoTotal = sumarPesos(x, diccionarioObjeto)
     print("la suma de todos los pesos de esta solucion es: ", pesoTotal, "grs")
     print()
     valido = verificarRestriccion(pesoTotal)
     if valido:
         listaSolucionesValidas.append(x)
print("Las soluciones que cumplen la restriccion son: ", listaSolucionesValidas)
print()
for i in listaSolucionesValidas:
    print("Solucion: ",i)
    v = calcularValor(i,diccionarioObjeto)
    print()
    listaValoresSoluciones.append(v)
    if (v > valorMaximo):
        valorMaximo = v
        solucionMaxima = i
#print (listaValoresSoluciones)
pesoMaximo = sumarPesos(solucionMaxima,diccionarioObjeto)
# valorMaximo = max(listaValoresSoluciones)
print("el valor mas alto es: $", valorMaximo, " con un peso de: ", pesoMaximo, "grs correspondiente a la solucion: ", solucionMaxima)

    
