distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km / velocidad_kmh
tiempo_semanas = int(tiempo_horas / 168)
tiempo_dias = int(tiempo_horas%168)
print(f"Tardarías {tiempo_semanas} semanas y {tiempo_dias} días en llegar.")