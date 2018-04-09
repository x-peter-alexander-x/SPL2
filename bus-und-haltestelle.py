#bus-und-haltestelle
p = 0
i = input("Wie viele Haltestellen")
for x in range (0, int(i)):
    z = input("Wie viele steigen ein?")
    a = input("Wie viele steigen aus?")
    p = p - int(a)
    p = p + int(z)
    if(p<60, p<=0):
        print("Invalide Anzahl von Personen im Bus")
        break
    else:
        print("Es sind ",p," Personen im Bus")
