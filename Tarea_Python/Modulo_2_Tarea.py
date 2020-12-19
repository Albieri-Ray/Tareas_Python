#Pregunta 1
"""
m=int(input("Ingrese un numero entero: "))
i=1
while i<=m:
    espacio = m-i
    print(' '*espacio+ "#"*i)
    i+=1
"""

#PREGUNTA 2
"""
texto = input("Mensaje cifrado > ").upper()
letras = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
# letras = "BCDEFGHIJKLMNÑOPQRSTUVWXYZA"
n=int(input("Ingrese cantidad: "))
for i in range(n):
    ciphertext = ""
    for l in texto:
        pos_letra = letras.index(l)
        nueva_pos = (pos_letra - n) % len(letras)
        ciphertext += letras[nueva_pos]
    msj = (f"caesar{n}:", ciphertext)
print(msj)
"""
#PROBLEMAS DIVERSOS
"""
1.Realizar una función que permita la carga de n alumnos. 
Por cada alumno se deberá preguntar el 
nombre completo y permitir el ingreso de 3 notas. 
Las notas deben estar comprendidas entre 0 y 10. 
Devolver el listado de alumnos."""
"""
def alumno(n):
    notas=[]
    nombre=[]
    for i in range(n):
        name= input(f'Ingrese el nombre del alumno {i+1}: ')
        nombre.append(name)
        nota_1 = float(input('Ingrese Nota 1: '))
        nota_2 = float(input('Ingrese Nota 2: '))
        nota_3 = float(input('Ingrese Nota 3: '))
        notas.append([nota_1,nota_2,nota_3])
    print("Alumnos \t Notas")
    for i in range(n):
        print(nombre[i],"\t \t",notas[i][0],notas[i][1],notas[i][2])
n=int(input("Ingrese cantidad de alumnos: "))
alumno(n)
"""

"""
2. Definir una función que dado un listado de alumnos evalúe cuántos 
aprobaron y cuántos desaprobaron, teniendo en cuenta que se aprueba con 4. 
La nota será el promedio de las 3 notas para cada alumno.
3. Informar el promedio de nota del curso total. """
"""
def alumno(n):
    notas=[]
    nombre=[]
    promedio=[]
    mensaje = []
    for i in range(n):
        name= input(f'Ingrese el nombre del alumno {i+1}: ')
        nombre.append(name)
        nota_1 = float(input('Ingrese Nota 1: '))
        nota_2 = float(input('Ingrese Nota 2: '))
        nota_3 = float(input('Ingrese Nota 3: '))
        prom= float((nota_1+nota_2+nota_3)/3)
        if prom > 3:
            mens= "Aprobo"
            mensaje.append([mens])
        else:
            mens= "Desaprobo"
            mensaje.append([mens])
       # prom= (notas[i][0]+notas[i][1]+notas[i][2])/3
        promedio.append([prom])
        notas.append([nota_1,nota_2,nota_3])        
    print("Alumnos \t Notas \t Promedio \t Estado")
    for i in range(n):
        print(nombre[i],"\t \t",notas[i][0],notas[i][1],notas[i][2],"\t \t",promedio[i],"\t \t",mensaje[i])
n=int(input("Ingrese cantidad de alumnos: "))
alumno(n)
"""