#nazwa_ostatni_znak = "nazwa nazwa"
#if nazwa_ostatni_znak == "":
#    print("Nazwa null")
#else:
#    print(nazwa_ostatni_znak[-1])

#input


samochody = ['polonez','syrenka', 'garbus', 'multipla']
auto = raw_input('Jakie masz auto?:  ')
i=[:]

Porownanie = [i for i in samochody if i in auto]

if i is None:
    print ("mamy to auto")
else:
    print("nie mamy auta")
