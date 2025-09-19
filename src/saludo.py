nombre=input("¿Como te llamas? ")
from datetime import datetime

hora_actual = datetime.now().hour

if 12>hora_actual:
    print("Buenos dias, ", nombre)
else:
    if hora_actual<20:
        print("Buenas tardes, ", nombre)
    else:
        print("Buenas noches", nombre)