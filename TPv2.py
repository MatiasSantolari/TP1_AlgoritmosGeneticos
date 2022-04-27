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
    return funcObj # lo que retorna es un valor flotante despues de aplicar la funcion objetivo


def fitness(x, subLista) -> float: #x es el valor de la funcion objetivo de un solo cromosoma
    return x / sum(subLista)


def binarioAdecimal(subLista): #sublista es listaPoblacionInicial que es la lista de cromosomas en formato entero
    listaDec = []
    for i in range(len(subLista)):
        cr = str(subLista[i]) #convierto un cromosoma entero de la lista en string
        a = int(cr, 2) #SI el cromosoma empieza con 0 tira error en la conversion de entero binario a decimal
        listaDec.append(a) #se crea una lista que contiene a los cromosomas en valor decimal en formato entero
    return listaDec


def aplicarFunObj(subLista): #Aca sublista es listaDecimales que es la lista que contiene a los cromosomas en valor decimal correspondiente en formato entero
    listaF = []
    for m in range(len(subLista)):
        f = funcionObjetivo(int(subLista[m])) #OBS: subLista[m] es un cromosoma en su valor decimal en la posicion m en formato entero
                                                # en reduntante pedir que se convierta un entero a entero
        listaF.append(f) #listaF va a ser una lista que contiene el valor de un cromosoma aplicando la Funcion Objetivo en formato FLOTANTE
    return listaF #retornamos la lista con todos los valores de la funcion objetivo del correspondiente cromosoma (segun su posicion) en formato FLOTANTE


def aplicarFitness(subLista): #Aca sublista es listaFunObj que es la lista que contiene los valores en formato entero de la funcion objetivo de cada cromosoma 
    listaFit = []
    for m in subLista:
        f = fitness(m, subLista) #m contiene el valor entero en la posicion de subLista
        listaFit.append(f) #listaFit es una lista con los valores de la fitness de cada cromosoma en forma flotante(ya que lo que retorna a funcion fitness es el valor en flotante)
    return listaFit  # retorna una lista de los valores de la funcion Fitness aplicadas a los cromosomas en formato flotante


def suma(lista):  # suma todos los valores de la funcion objetivo de cada cromosoma
    cont = 0
    for u in range(len(lista)):
        cont += lista[u]
    return cont


def promedio(lista):  # me devuelve el promedio de la listaFunjObj que es la lista que contiene los valores en formato ENTERO de la funcion objetivo de cada cromosoma 
                        # ( mas adelante tambien se trabaja con la lista de la funcion fitness que es uan lista con los valores FLOTANTES de la funcion fitness de cada cromosoma)
    suma = 0
    for u in range(len(lista)):
        suma += lista[u] #suma tiene el valor a sumar todos los valores 
    promedio = suma / len(lista)
    return promedio #promedio vuelve como un dato en formato FLOTANTE (ya sea que se trabajo con listaFunObj como listaFitness)


def maximo(lista):  # devuelve el valor maximo de la lista funcion objetivo (y mas adelante tambien se trabaja con la lista de la funcion fitness) en formato FLOTANTE
                    # ( mas adelante tambien se trabaja con la lista de la funcion fitness y lo que retorna tambien es un valor FLOTANTE)
    return max(lista)

def minimo(lista): # devuelve el valor minimo de la lista funcion objetivo en formato FLOTANTE
                    # ( mas adelante tambien se trabaja con la lista de la funcion fitness y lo que retorna en un valor FLOTANTE)
    return min(lista)

def cromoMaximo(listaPoblacionInicial):
    valor = listaPoblacionInicial[9] #como listaPoblacionInicial esta ordenada de menor a mayor, siempre vamos a queres el cromosoma en la ultima posicion(que en esta caso es 9) que seria 
                                     #el cromosoma con el valor de la funcion objetivo mas alto
    return valor #valor contiene el cromosoma en formato ENTERO con mayor valor de la funcion objetivo

# -----------------------------------------------------------------------------------------------------------
# En esta seccion se van a ver las funciones o lo relacionado con la seleccion, crossover y mutacion

def partRuleta(listaFitness):  # se calcula el porcentaje de cada cromosoma y se le asigna
                                # un arco de circunferencia proporcional a su fitness. porc
                                #El parametro es la listaFitness que es uan lista con los valores en formatO FLOTANTE de la funcion fitness aplicada a cada cromosoma
    i = 0
    listaPorcentajeFitness = []
    for b in range(len(listaFitness)):
        den = sum(listaFitness)
        nu = round((listaFitness[i] / den) * 100, 2)
        listaPorcentajeFitness.append(nu) 
        i += 1
    return listaPorcentajeFitness #listaProcentajeFitness es una lista que va a tener los porcentajes en formato FLOTANTE de cada cromosoma segun su valor de la funcion fitness

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

def seleccionRuleta(ruleta, posiciones, poblacion): #ruleta es la lista de valores ENTEROS de los porcentajes de los cromosomas segun su funcion fitness 
                                                    #posiciones es int(sum(ruleta)) que seria el valor ENTERO de la suma de los valores de la lista ruleta.
                                                    #poblacion es listaPoblacionInicialCadena que es la lista de los cromosomas en digitos binarios en formato STRING
    ruletaDefinitiva=[] #es la lista de 100 posiciones en donde a cada posicion de esta lista se le asigna el cromosoma en formato STRING en la posicion i de la lista poblacion
    padres=[] #es la lista con los cromosomas en formato STRING que fueron seleccionados en la lista ruletaDefinitiva, que serian los padres
    for i in range(10):
        for j in range(ruleta[i]):
            ruletaDefinitiva.append(poblacion[i])
    for k in range(10):
        a = random.randint(0, posiciones) # genera un numero entero entre 0 y posiciones (que seria 100 aprox). Seria la "Tirada de la bolita en la ruleta"
        padres.append(ruletaDefinitiva[a]) # se agrega en padres el cromosoma en formato STRING en la lista ruletaDefinitiva en la posicion elegida aleatoriamente. Seria "El lugar donde cayo la bola al girar la ruleta"
    return padres #es la lista con los cromosomas en formato STRING que fueron seleccionados en la lista ruletaDefinitiva al girarla 10 veces, ya que los padres deben ser 10

"""def seleccionCrossover(padres):
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

    #entre el 1 y el 2:
    a = random.uniform(0, 1)
    if (a <= probabilidadCrossover):
        listaHijos.append(aplicarCrossover(padres[1],padres[2]))
    else:
        listaHijos.append(padres[1])
        listaHijos.append(padres[2])

    for i in range(5): #que se hace en este for
        for j in padres:
            a = random.randint(0, 1)
        if (a <= probabilidadCrossover):
            pass
        else:
            listaHijos.append()
        
    return


def seleccionMutacion():
    return

def aplicarCrossover(padre1,padre2):
    aux=[]
    a = random.randint(0, 29)

    for j in range(a):
        aux.append(padre1[j])

    for i in range(a, len(padre1)):
        aux.append(padre2[i])
        padre2[i] = padre1[i]

    return(aux,padre2)
"""

def seleccionCrossover(cromo1, cromo2): #cromo 1 y cromo 2 van a tener c/u el cromosoma en formato ENTERO donde cada posicion es un gen binario ENTERO y cromosoma es un padre (ya convertido a ENTERO) de la listaPadres 
   
    a = random.uniform(0, 1) #La función random.uniform devuelve un número real entre 0 y 1
    if (a <= probabilidadCrossover):
        rango = random.randint(0, 29) #random.randint devuelve número entero aleatorio en el intervalo cerrado (tambien toma los limites) entre 0 y 29
        aux1 = cromo1[:rango] + cromo2[rango:] #con el [:rango] selecciona los valores de rango
        aux2 = cromo2[:rango] + cromo1[rango:] #aca se generan los hijos es decir los padres aplicando crossover
        cromo1 = aux1  #esos hijos se guardan donde anteriormente estaban los padres
        cromo2 = aux2
    return cromo1, cromo2 # cromo 1 y cromo2 son listas que contienen valores ENTEROS donde cada valor es un gen, es decir c1 y c2 son un Cromosoma

def mutacion(cromo1): #le paso el cromosoma despues de haber con el croosover (puede que no se haya aplicado) y cromo es una cromosoma que a la vez es una lista de genes donde c/gen es un ENTERO binario
    d = random.uniform(0, 1)
    if (d <= probabilidadMutacion):
        i = random.randint(0, 29) #determinar una posicion al azar del cromosoma entre 0 a 29 (incluyendo 0 y 29)
        if(cromo1[i]==0):
            cromo1[i]=1
        else:
            cromo1[i]=0
    return cromo1 #cromo1 es un cromosoma, que a la vez es una lista de genes donde c/gen es un ENTERO binario
        

# Aca inicia el main del TP
i = 0
poblacion = []
lista = []
listaPoblacionInicialCadena = [] #lista de cromosomas binarios en formato string 
listaPoblacionInicial = [] #lista de cromosomas con digitos binarios en formato enteros
listaDecimales = [] # lista que contiene a los cromosomas en valor decimal correspondiente en formato entero
listaFunObj = [] #lista que contiene los valores en formato FLOTANTE de la funcion objetivo de cada cromosoma correspondiente a la posicion en listaDecimales
listaFitness = [] #lista de los valores de la funcion Fitness aplicadas a los cromosomas de la listaFunObj en formato flotante
listaPadres = [] #lista que tiene los cromosomas en formato STRING que seran los padres para obtener a los hijos de la siguiente generacion
listaSiguienteGeneracion = [] #lista que tiene listas en donde c/u de esas listas es un cromosoma, es decir, es una lista de 30 posiciones donde cada posicion es un gen ENTERO binario
maxiObj = 0 #contiene el valor maximo de la funcion objetivo del cromosoma en la listaFuncObj en formato FLOTANTE
miniIbj = 0 #contiene el valor minimo de la funcion objetivo del cromosoma en la listaFuncObj en formato FLOTANTE
prome = 0 #contiene el promedio de la lista que tiene los valores de la funcion objetivo de cada cromosoma, es decir de la poblacion, en formato FLOTANTE
cromosomaMaximo = 0 #contiene el cromosoma binario en formato ENTERO con el mayor valor de la funcion objetivo

def funcionPrincipal(listaPoblacionInicial, listaPoblacionInicialCadena):
    
    listaDecimales.extend(binarioAdecimal(listaPoblacionInicial)) #listaDecimales es una lista que contiene
    print("Los numeros decimales de cada cromosoma correspondiente son ", listaDecimales)
    print()
    listaFunObj.extend(aplicarFunObj(listaDecimales)) #listaFunObj es la lista que contiene los valores en formato FLOTANTE de la funcion objetivo de cada cromosoma correspondiente a la posicion en listaDecimales
    print("valor de la funcion objetivo de cada cromosoma:", listaFunObj)
    print()
    listaFitness.extend(aplicarFitness(listaFunObj)) #listaFitness es una lista en formato FLOTANTE con el valor de la funcion fitness aplicada a cada cromosoma de la lista listaFunObj
    print("fitness", listaFitness)
    print()
    print("la suma de todos los valores de la funcion objetivo es: ", suma(listaFunObj))
    print()
    
    # estos 7 valores son con respecto a una poblacion
    maxiObj = maximo(listaFunObj) #retorna el valor maximo de la lista que tiene los valores de la funcion objetivo de cada cromosoma en formato FLOTANTE
    cromosomaMaximo = cromoMaximo(listaPoblacionInicial)
    miniObj = minimo(listaFunObj) #retorna el valor minimo de la lista que tiene los valores de la funcion objetivo de cada cromosoma en formato FLOTANTE
    promeObj = promedio(listaFunObj) #retorna el promedio de la lista que tiene los valores de la funcion objetivo de cada cromosoma en formato FLOTANTE
    maxiFit = maximo(listaFitness) #retorna el valor maximo de la lista que tiene los valores de la funcion fitness de cada cromosoma en formato FLOTANTE
    miniFit = minimo(listaFitness)
    promeFit = promedio(listaFitness)
    #
        
    tabla = pd.DataFrame( 
        {'pobl': listaPoblacionInicial, 'X': listaDecimales, 'F obj': listaFunObj, 'Fitness': listaFitness})
    print(tabla)
    print(cromosomaMaximo, ' ',maxiObj ,' ', miniObj, ' ', promeObj,' ',maxiFit, '', miniFit,' ',promeFit)

    #Luego de mortar la tabla con PoblacionInicial, sus decimales, sus valores de la funcion objetivo y de la fitness
    #Hay que mostrar el Cromosoma correspondiente al valor máximo, el valor máximo, mínimo y promedio obtenido de cada población.
    # X las dudas mostramos el maximo, minimo y promedio de la funcion objetivo y fitness
    print()
    print('los porcentajes de cada cromosoma dependiendo de su funcion fitnes es', partRuleta(listaFitness))
    print()

    ruleta = [] # lista de los valores en formato ENTERO de los porcentajes redondeados de la funcion fitness
    for i in partRuleta(listaFitness): #esta funcion trae una lista que va a tener los porcentajes en formato FLOTANTE de cada cromosoma segun su valor de la funcion fitness
        if i > 1:
            n = round(i, 0) #n va a tener el valor en formato ENTERO redondeado del porcentaje relacionado a la funcion fitness
            ruleta.append(int(n))
        else:
            ruleta.append(1)

    print('redondeo de los procentajes de cada cromosoma dependiendo de su funcion fitnes y que no haya perocentajes menores a 1:', ruleta)
    print()
    print('comprobacion que la suma de los porcentajes da 100:',int(sum(ruleta)))
    print()
    listaPadres.extend(seleccionRuleta(ruleta, int(sum(ruleta)), listaPoblacionInicialCadena))
    print('La lista de los padres es: ',listaPadres) #listaPadres tiene los cromosomas en formato STRING para aplicar el Crossover y Mutacion
    
    '''print("Prueba cadena")
    print(listaPoblacionInicial)
    print(listaPoblacionInicialCadena)'''
    
    #OBSERVACION: Las cadenas son inherentemente iterables, lo que significa que la iteración sobre una cadena da cada carácter como salida.
    z=0
    for i in range(5): #se repite 5 veces xq hay 5 pares de cromosomas padres para aplicar el crossover
        c1= [int(x) for x in str(listaPadres[z])] # c1 es una lista en formato ENTERO donde cada posicion contiene un gen, es decir c1 es un cromosoma padre
        c2 = [int(x) for x in str(listaPadres[z+1])] # c2 es una lista en formato ENTERO donde cada posicion contiene un gen, es decir c2 es un cromosoma padre
        hijo1, hijo2 = seleccionCrossover(c1, c2) # hijo1 y hijo son listas de Enteros donde cada posicion es un gen entero. hijo1 y hijo2 son cromosoma 
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        z += 2 #con la variable z me ubico a cada par de posicion en el arreglo padre
        print(hijo1)
        print(hijo2)
        listaSiguienteGeneracion.append(hijo1)
        listaSiguienteGeneracion.append(hijo2)
    print (listaSiguienteGeneracion)
    return (listaSiguienteGeneracion)
    

#Se creau una sola vez la poblacion inicial (definir los cromosomas...)
nuevaGeneracion #lista de cromosomas donde cada cromosoma es una lista de ENTEROS
for j in range(10):
    cromo = definirCromosoma() #definirCromosoma devuelve los 30 digitos binarios pero en formatio string
    listaPoblacionInicialCadena.append(cromo) # esta lista es una lista de cromosomas en formato string 
    num = int(cromo) #num tiene el cromosoma pero en formato entero 
    listaPoblacionInicial.append(num) #esta lista es una lista de cromosomas en formato enteros
print("Los cromosomas seleccionados son ", listaPoblacionInicial)  # contiene los cromosomas en formato enteros
listaPoblacionInicial.sort() # con la funcion sort ordena la lista de menor a mayor
listaPoblacionInicialCadena.sort()
print()
print()
for p in range(20):
    # PASAR DE FORMATO LISTA DE LISTA DE ENTEROS BINARIOS A LISTA DE ENTEROS Y LISTA DE STRING 
    nuevaGeneracion = funcionPrincipal(listaPoblacionInicial, listaPoblacionInicialCadena)
    
    listaPoblacionInicial = nuevaGeneracion
    

"""Al finalizar el programa tiene que mostrar
   el Cromosoma correspondiente al valor máximo, el valor máximo, mínimo y 
   promedio obtenido de cada población.
"""



"""for i in range (20): # se hace las 20 corridas de la funcion
    funcionPrincipal()"""
    



