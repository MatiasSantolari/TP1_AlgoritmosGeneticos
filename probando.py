import random

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
print (aux)




