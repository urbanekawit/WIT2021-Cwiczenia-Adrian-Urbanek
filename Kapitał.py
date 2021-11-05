x=float(input("Podaj kapitał początkowy (PLN) "))
y=float(input("Podaj miesięczne wpływy (PLN) "))
z=int(input("Przez ile miesięcy zamierzasz inwestować? "))
w=float(input("Jak dużo na koniec ma być warta inwestycja? (PLN) "))
i=0
while (i<z):
    i=i+1
    k=(2/100)*x
    l=float(k+x)
    x = x + y + k
if (l>w):
    print(f"Inwestycja jest warta więcej niż zakładano i wynosi {round(l,2)}")
elif (w>l):
    print(f"Inwestycja jest warta mniej niż zakładano i wynosi {round(l,2)}")
if (w==l):
    print(f"Inwestycja jest warta tyle ile zakładano i wynosi {round(l,2)}")