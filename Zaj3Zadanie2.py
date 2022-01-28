lista=[1,2,3,4,5]
le=sorted(lista)
a=len(le)-1
lmax=[]
i=2
while i>0:
    lmax.append(le[a])
    a=a-1
    i=i-1
lmax.sort()
print(f"lista_max = {lmax}")








