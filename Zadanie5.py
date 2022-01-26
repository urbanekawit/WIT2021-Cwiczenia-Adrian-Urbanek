lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
lista3=[1,2,3,3,4,5]
if set(lista1) == set(lista2) and set(lista3) == set(lista3):
        print('Wszystkie listy zawieraja takie same elementy')

if len(lista1)!=len(set(lista1)):
    print('lista1 zawiera duplikaty')
if len(lista2)!=len(set(lista2)):
    print('lista2 zawiera duplikaty')
if len(lista3)!=len(set(lista3)):
     print('lista3 zawiera duplikaty')
len(set(lista3))
