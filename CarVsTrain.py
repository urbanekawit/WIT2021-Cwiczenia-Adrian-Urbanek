print("Pociąg z miejscowości A do miejscowości B pokonuje drogę 250km w czasie 2h 45min.")
x=int(input("Podaj średnią prędkość z jaką będziesz się poruszał i sprawdź czy będziesz szybszy :P "))
p=250/(165/60)
if (p>x):
    print("Pociąg dojedzie szybciej, lepiej kup bilet. ")
else:
    print("Pociąg dojedzie wolniej, tankuj do pełna. ")
