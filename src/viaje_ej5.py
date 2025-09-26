clave=True

while clave==True:

    distancia_km = int(input("¿Cuanta distancia quieres viajar? (En kilómetros) "))
    velocidad_kmh = int (input("¿Cuanta velocidad vas a tomar? (En kilómetros/hora)"))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    clave2=input(("¿Quieres hacer otra simulación? (s/n)"))
    if clave2=="n":
       clave=False
    else:
        print("Siguiente simulación")