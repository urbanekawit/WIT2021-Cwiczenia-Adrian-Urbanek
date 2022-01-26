lista=[1,2,3,4,5]
odwrocona_lista=lista
i=1
a=len(odwrocona_lista)
while i<=a:
    b=odwrocona_lista[a-i]
    del(odwrocona_lista[a-i])
    odwrocona_lista.append(b)
    i=i+1
print(f"odwrocona lista = {odwrocona_lista}")