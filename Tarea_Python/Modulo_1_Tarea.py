#Pregunta 1
"""
print("¿Cual es tu nombre?")
nombre = input()
print("Hola " + nombre)
"""
#Pregunta 2
"""
import string

clave = 'VCHPRZGJNTLSKFBDQWAXEUYMOI'
alfabeto = string.ascii_uppercase

plaintext = input('ingrese la palabra a encripta: ')
ciphertext = ''

for plaintext in plaintext.upper():
    for a in alfabeto:
        if plaintext ==a:
            ciphertext += clave[alfabeto.index(plaintext)]
print(ciphertext)    
"""

#Preguntas adicionales
#Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y 
# la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

#Kilómetros recorridos: 260
#Litros de combustible gastados: 12.5
#El consumo por kilómetro es de 20.8
"""
kilometro = float(input("Ingrese cantidad de Kilómetros: "))
litro = float(input("Ingrese los litros de combustible consumidos: ")) 
calculo = kilometro/litro
print("El consumo por kilómetro es de: ",calculo)  
"""


# Escriba un programa que pida los coeficientes 
# de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.


"""
print("Ingrese los coeficientes de la ecuación de segundo grado")

a= float(input("El valor a: "))
b= float(input("El valor b: "))
c= float(input("El valor c: "))
resultado = 0
descriminante = float((b*b) - (4*a*c))
if a == 0:
    resultado = -1 * (c/b) 
    print ("El valor de X es: ", resultado)
elif descriminante > 0:
    calculo_posi = float((-b+pow(pow(b,2)-(4*a*c),1/2))/ (2*a))
    calculo_nega = float((-b-pow(pow(b,2)-(4*a*c),1/2))/ (2*a)) 
    print ("Los valores de X son: ",str(calculo_posi) + " y ",str(calculo_nega))
elif descriminante < 0:
    print ("No tiene solución real")
elif descriminante == 0:
    calculo = float((-b)/(2*a))
    print ("Doble Solución de valor(+/-): ",-1*calculo)
"""

"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no"""
"""
edad= int(input("Cuantos años tienes: "))

if edad>=18:
    print('Usted es mayor de edad')
else:
    if edad > 0:
        print('Usted es menor de edad')
    else:
        print('Edad no válida')
"""