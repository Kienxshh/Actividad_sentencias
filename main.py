INDIVIDUAL = 40000
DOBLE = 65000
SUITE = 100000

nombre = input("Ingrese su nombre\n")
tipo_habitacion = int(input("Ingrese tipo de habitacion"))
cantidad_noche = int(input("Ingrese cantidad de noches\n"))
edad = int(input("Ingrese su edad\n"))
es_miembro = input("Es miembro del hotel? si - no\n").lower()


if tipo_habitacion == 1:
    habitacion = INDIVIDUAL
elif tipo_habitacion == 2:
    habitacion = DOBLE
elif tipo_habitacion == 3:
    habitacion = SUITE
else:
    habitacion = 0

    valor_inicial = habitacion * cantidad_noche

if edad > 0 and edad < 18:
    descuento = 0.90
    porcentaje_edad = 10
    
elif edad >= 65:
    descuento = 0.85
    porcentaje_edad = 15
else:
    descuento = 1
    porcentaje_edad = 0
valor_provisorio = valor_inicial * descuento

if es_miembro == "si":
    valor_precio_miembro = valor_provisorio * 0.90
    porcentaje_miembro = 10
else:
    valor_precio_miembro = valor_provisorio * 1
    porcentaje_miembro = 0


if cantidad_noche >= 7:
    valor_precio_noche = valor_precio_miembro * 0.95
    porcentaje_noche = 5
else:
    valor_precio_noche = valor_precio_miembro * 1
    porcentaje_noche = 0


print(f"Precio Inicial: ${valor_inicial}")
print(f"Descuento Edad: {porcentaje_edad}")
print(f"Precio: ${valor_provisorio}")
print(f"Descuento de Miembro: 10%")
print(f"Precio: ${valor_precio_miembro}")
print(f"Descuento por noche: {porcentaje_noche}")
print(f"Precio final a pagar: ${valor_precio_noche}")