#bus-und-haltestelle
p = 0
i = input("Wie viele Haltestellen")
for x in range (0, int(i)):
    z = input("Wie viele steigen ein?")
    a = input("Wie viele steigen aus?")
    p = p - int(a)
    p = p + int(z)
    if(p>60):
        print("Zu hohe Anzahl von Personen im Bus")
        break
    elif(p<0):
        print("Weniger als 0 Personen")
    else:
        print("Es sind ",p," Personen im Bus")
