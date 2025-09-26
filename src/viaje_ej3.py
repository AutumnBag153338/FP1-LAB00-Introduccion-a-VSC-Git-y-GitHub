edad=int(input("¿Cuál es tu edad? "))
nivel=int(input("¿Del uno al 10, cuál consideras que es tu nivel físico? "))
if edad>18:
    print("Tienes edad suficiente")
    if nivel>5:
        print("¡Listo para despegar!")
    else:
        print("Debes estar en mejor forma.")
else:
    print("Debes ser mayor de edad.")
