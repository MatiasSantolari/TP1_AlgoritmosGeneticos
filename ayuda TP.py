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
print(padres) #es la lista con los cromosomas en formato STRING que fueron seleccionados en la lista ruletaDefinitiva al girarla 10 veces, ya que los padres deben ser 10"""

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
print(c)


