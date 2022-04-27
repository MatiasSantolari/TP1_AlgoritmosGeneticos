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









