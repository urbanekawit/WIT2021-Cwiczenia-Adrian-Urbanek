a=int(input("Podaj liczbę a: "))
b=int(input("Podaj liczbę b: "))
c=a
d=b
while not (a == b):
    if a<b:
        a=a+c
    else:
        b=b+d
e=b
print(f"Najmniejsza wieloktrotność liczb {c} i {d} wynosi: {e} ")


