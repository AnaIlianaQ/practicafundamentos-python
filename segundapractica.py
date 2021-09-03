
# nombre = input ("introduce tu nombre: ")
# print(f"hola {nombre}")
# cadena de caracteres
# entero
edad = 22
# flotante - decimales
altura = 1.75
# convertir a flotante
edadString = str(edad)
print(edad + edad)
print(edadString + edadString)
tuEdad = input("introduce tu edad: ")
tuEdad = int(tuEdad)

#estructura de control if
if tuEdad >= 18 and tuEdad < 100:
    print("eres mayor de edad")
elif tuEdad >= 100:
    print("¿Eres inmortal?")
elif tuEdad <= 0:
    print("No existes jaja")
else:
    print("Eres menor de edad")

#estructura de control for    
for i in range(0,10):
    print(i)

#estructura de control Switch
dia = input("Introduce un dia: ")
dia =int (dia)

with switch(dia) as s:
    if s.case(15):
        print("Es quinccena :D")
        