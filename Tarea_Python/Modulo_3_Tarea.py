#Pregunta 1
"""
def s_digitos(num):
    if (num==(num%10)):
        return num
    else:
        return (num%10)+ s_digitos(int(num/10))
Ntarjeta= ""
def v_tarjeta():
    Reverse_Num_Tarjeta = Ntarjeta[::-1]
    suma=0
    for i in range(1,len(Reverse_Num_Tarjeta),2):
        suma+=s_digitos(int(Reverse_Num_Tarjeta[i])*2)
    for i in range(0,len(Reverse_Num_Tarjeta),2):
        suma+=int(Reverse_Num_Tarjeta[i])
    if (suma%10)==0:
        return True
    else:
        return False
def t_tarjeta():
    if Ntarjeta.startswith("34") or Ntarjeta.startswith("37"):
        return "AMEX"
    elif Ntarjeta.startswith("51") or Ntarjeta.startswith("52") or Ntarjeta.startswith("53") or Ntarjeta.startswith("54") or Ntarjeta.startswith("55"):
        return "MASTERCARD"
    elif Ntarjeta.startswith("4"):
        return "VISA"
    else:
        return "Numero invalido"

if __name__ == "__main__":
    Ntarjeta=input("Ingrese número de tarjeta: ")
    if v_tarjeta():
        print(t_tarjeta())
    else:
        print("Numero invalido")
"""

#PROBLEMAS DIVERSOS
"""
Cantidad=0
Lista_Alumno= list()
def register_nota(nota_d):
    while True:
        nota=int(input(f"Ingrese la nota {nota_d}: "))
        if nota>=0 and nota<=10:
            return nota
        else: 
            print ("Nota fuera de rango")
def datos_alumnos():
    for contador in range(Cantidad):
        Alumno = {
        'Nombre':'',
        'Notas':[0,0,0],
        'Promedio':0
        }
        Alumno['Nombre']=input('Ingrese nombre del alumno: ')
        Alumno['Notas'][0]=register_nota(1)
        Alumno['Notas'][1]=register_nota(2)
        Alumno['Notas'][2]=register_nota(3)
        Lista_Alumno.append(Alumno)
def apro_repro():
    aprobados=0
    desaprobados=0
    total=0
    for i in range(Cantidad):
        Alumno=Lista_Alumno[i]
        p = sum(Alumno['Notas'])/len(Alumno['Notas'])
        Alumno['Promedio']=p
        total+=p
        if p < 4:
            desaprobados +=1
        else:
            aprobados +=1
    print(f"La cantidad de alumnos aprobados es {aprobados} y desaprobados es {desaprobados}")
    print(f"El promedio de las notas es {total/Cantidad}")
        
def Promedio(prom):
    return prom['Promedio']

def mayor_menor():
    Lista_sort=sorted(Lista_Alumno, key=Promedio)
    print("El mayor promedio fue el alumno : " + Lista_sort[-1]['Nombre'])
    print("El menor promedio fue el alumno : " + Lista_sort[0]['Nombre'])

def buscar():
    buscar_alumno=input('Buscar alumno (Nombre): ')
    busqueda=list([alumno for alumno in Lista_Alumno if alumno['Nombre'].upper().find(buscar_alumno.upper())>=0])
    if len(busqueda)>0:
        print("Alumnos con el nombre digitado :")
        print(busqueda)
    else:
        print("Cero coincidencias")
if __name__ == "__main__":

    Cantidad=int(input('Ingrese la cantidad de alumnos del curso: '))
    print("\n1. Registro de datos de los alumnos")
    datos_alumnos()
    print("\n2. Alumnos aprobados y desaprobados")
    apro_repro()
    print("\n3. Alumnos mayor y menor promedio")
    mayor_menor()
    print("\n4. Buscar alumnos")
    buscar()
"""