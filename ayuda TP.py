import random
'''num = 1010
print (str(num))
lis = list(map(int,str(num)))
print(lis)

n=0
lista=[]
for i in range(5):
    lista.append([n,n+1])
    n+=2
print(lista)

a=0
nu=101
st = str(nu)
a = int(st, 2)
print (a)



for i in range(5):
        for j in padres:
        a = random.randint(0, 1)
        if (a <= probabilidadCrossover):
            pass
        else:
            listaHijos.append()'''
"""listaFunObj = [3, 5, 10]
            
def promedio(listaFunObj):  # calcula el promedio
    suma = 0
    for u in range(len(listaFunObj)):
        suma += listaFunObj[u]
    promedio = suma / len(listaFunObj)
    return promedio
print(promedio(listaFunObj))"""#

"""ruleta = [1,1,1,1, 3, 4, 6, 15, 22, 46]
poblacion = ["a","b","c","d","e","f","g","h","i",'j']
posiciones = int(sum(ruleta))
pos = 0

ruletaDefinitiva=[] #es la lista de 100 posiciones en donde a cada posicion de esta lista se le asigna el cromosoma en formato STRING en la posicion i de la lista poblacion
padres=[] #es la lista con los cromosomas en formato STRING que fueron seleccionados en la lista ruletaDefinitiva, que serian los padres
print(len(ruleta))
print(posiciones)
for i in range(len(ruleta)):
   # print("i:",i)
   # print(poblacion[i])
    for j in range(ruleta[i]):
       # print(poblacion[i])
       # print("j",j)
        ruletaDefinitiva.append(poblacion[i]) #el tamaño de ruletaDefinitiva es posiciones->int(suma(ruleta))
        print("reluta definitiva en posicion ",pos," es ",ruletaDefinitiva[pos])
        pos+=1
for k in range(10):
    a = random.randint(0, posiciones-1) # genera un numero entero entre 0 y posiciones (que seria 100 aprox). Seria la "Tirada de la bolita en la ruleta"
    print(a)
    padres.append(ruletaDefinitiva[a]) # se agrega en padres el cromosoma en formato STRING en la lista ruletaDefinitiva en la posicion elegida aleatoriamente. Seria "El lugar donde cayo la bola al girar la ruleta"
print(padres) #es la lista con los cromosomas en formato STRING que fueron seleccionados en la lista ruletaDefinitiva al girarla 10 veces, ya que los padres deben ser 10

def elitismo(listaPoblacionInicialCadena, listaFitness):
    listaFit=listaFitness.copy()
    cromosomasSeleccionados=[]
    for d in range(2):
        fitMax = max(listaFit)
        print(fitMax)
        indice = listaFit.index(fitMax) #Los otros elementos con el mismo valor se ignoran porque ya ha encontrado una coincidencia dentro de la lista.
        print("indice donde esta el valor maximo en listaFit: ",indice)
        cromosomasSeleccionados.append(listaPoblacionInicialCadena[indice])
        listaFit[indice] = 0
        print("listaFit al sacar el maximo: ",listaFit)
    return cromosomasSeleccionados

a = ["a", "b", "c", "e", "f"]
b = [4,6,6,3,2]
c = elitismo(a, b)
print(c)"""
#------------------------------------------------------------------------------------------------
#Esta funcion es para la seleccion con el metodo torneo para la OPCION C
a = ["a","b","c","d","e","f"]
b = [4,9,2,3,7,4]
def seleccionTorneo(listaPoblacionInicalCadena, listaFitness): #tengo que devolver la lista de padres en formato STRING
   
    largo=[]
    listaGanadores=[]
    listaParticipantes=[]
    listaIndicesParticipantes=[]
    listaFitnessParticipantes=[]
    k = 3
    
    for q in range(k): # k es la cantidad de veces que se repite la seleccion por torneo
        largo.clear()
        listaParticipantes.clear()
        listaIndicesParticipantes.clear()
        listaFitnessParticipantes.clear()
    
        for t in range(len(listaPoblacionInicalCadena)): #aca genero la lista de los indices de listaPoblacionInicialCadena para trabajar mas tarde con el Fitness
            largo.append(t)
            print(largo) #largo tiene todos los indices de listaPoblacionInicialCadena
            print()
        for e in range(5):# 5 es la cantidad de individuos para seleccion torneo (el grupo de participantes)
            indiceParti= random.choice(largo) #elijo a los participantes que van a estar en el torneo
            print("indice del participante seleccionado que hace referencia a la posicion en listaPoblacionIncialCadena es: ",indiceParti)
            print()
            listaIndicesParticipantes.append(indiceParti)
            print("lista de indices de los participantes seleccionados en listaPoblacionInicialCadena: ",listaIndicesParticipantes)
            print()
            parti = listaPoblacionInicalCadena[indiceParti] #parti tiene el cromosoma en STRING que fue seleccionado para ser participante
            listaParticipantes.append(parti) #agrego los participantes que van a ir al torneo a esta lista
            print("participantes en la listaParticipantes: ", listaParticipantes)
            print()
            #ya esta conformado la lista con los 5 participantes, ahora tengo que seleccionar el que tiene el mayor fitness
        for o in listaIndicesParticipantes:
            print("lista indices participantes: ",listaIndicesParticipantes)
            print("valor de o: ", o)
            print()
            listaFitnessParticipantes.append(listaFitness[o])
            print("lista fitness de cada participante: ", listaFitnessParticipantes)
            print()
        maxfit = max(listaFitnessParticipantes)
        print("fitness maximo de la lista fitness participante: ", maxfit)
        indiceGanador = listaFitnessParticipantes.index(maxfit)
        print("el indice del ganador es: ", indiceGanador)
        print()
            
        listaGanadores.append(listaParticipantes[indiceGanador])
        print("lista ganadores en la iteracion",q+1," es ",listaGanadores)
  
    
    return listaGanadores

t = seleccionTorneo(a,b)


