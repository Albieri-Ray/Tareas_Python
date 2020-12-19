#Problemas Diversos
"""
def p1():
    while True:
        try:
            numero = int(input("Ingrese un número del rango 1 - 10:"))
            if numero >= 1 and numero <= 10:
                break
            else:
                print("El número esta fuera del rango (1-10)")
        except:
            print("Número invalido")
    
    with open(f'./tabla-{numero}.txt',mode='w') as f:
        for i in range(0, 11):
            f.write(f"{numero} x {i} = {numero*i}\n")
        print(f"El archivo tabla-{numero}.txt se creó en la ruta actual de forma satisfactoria")
        f.close
p1()
"""
"""
def view():
    while True:
        try:
            numero = int(input("Ingrese un número del rango 1 - 10:"))
            if numero >= 1 and numero <= 10:
                break
            else:
                print("El número esta fuera del rango (1-10)")
        except:
            print("Número invalido")
    try:
        with open(f'./tabla-{numero}.txt',mode='r') as f:
            texto = f.readlines()
            for fila in texto:
                print(fila)
    except:
        print("No existe ese valor")
view()
"""