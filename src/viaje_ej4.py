# Distancia a Marte en kilómetros
distancia_marte_km = 225000000

# Usamos un bucle 'for' con 'range' para ir de 10.000 a 50.000, en saltos de 10.000
for velocidad in range(10000, 50001, 10000):
  # Calcula el tiempo de viaje en horas
  tiempo_horas = distancia_marte_km / velocidad
  
  # Convierte las horas a días
  tiempo_dias = tiempo_horas / 24
  
  # Muestra el resultado con el formato pedido
  print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo_dias} días")
