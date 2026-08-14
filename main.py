# Actividad: Sistema de reservas del Hotel Sol
# Debes crear un programa en Python que calcule el precio final de una reserva en un hotel.
# Enunciado
# El Hotel Sol tiene las siguientes tarifas:
#•	Habitación individual: $40.000 por noche.
#•	Habitación doble: $65.000 por noche.
#•	Habitación suite: $100.000 por noche.
#El cliente debe ingresar:
#1.	Su nombre.
#2.	El tipo de habitación (individual, doble o suite).
#3.	La cantidad de noches.
#4.	Su edad.
INDIVIDUAL = 40000
DOBLE = 65000
SUITE = 100000
#SOLICITO TODOS LOS DATOS AL USUARIO
nombre = input("Ingrese su nombre\n")
tipo_habitacion = int(input("Ingrese tipo de habitacion"))
cantidad_noche = int(input("Ingrese cantidad de noches\n"))
edad = int(input("Ingrese su edad\n"))
es_miembro = input("Es miembro del hotel? si - no\n")

#El programa debe calcular el precio de la estadía y aplicar los siguientes descuentos:
#•	Si el cliente tiene menos de 18 años, recibe un 10% de descuento.
#•	Si tiene 65 años o más, recibe un 15% de descuento.
# Debo asignar valor a una variable auxiliar para obtener los montos de los tipos de habitacion
if tipo_habitacion == 1:
    habitacion = INDIVIDUAL
elif tipo_habitacion == 2:
    habitacion = DOBLE
elif tipo_habitacion == 3:
    habitacion = SUITE
else:
    habitacion = 0

if edad > 0 and edad < 18:
    descuento = 0.90
    
elif edad >= 65:
    descuento = 0.85
    
else:
    descuento = 1
valor_provisorio = habitacion * descuento

#•	Si es miembro del hotel, recibe un 10% de descuento adicional.
#•	Si la estadía es de 7 noches o más, recibe un 5% de descuento adicional.
# Importante
# Los descuentos se aplican sobre el precio que queda después del descuento anterior.
# Por ejemplo:
# Precio inicial: $500.000
# Descuento de edad: 10%
# Precio: $450.000
# Descuento de miembro: 10%
# Precio final: $405.000
