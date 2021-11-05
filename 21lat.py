x=int(input("W jakim jesteś wieku? "))
if (x>=21):
    print("Możesz prowadzić samochód oraz głosować w wyborach")
else:
    if(x>=17):
        print("Możesz prowadzić samochód")
    else:
        print("Nie możesz głosować ani prowadzić samochodu")