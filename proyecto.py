


def menu():
    print("\t|1.- Comprar boleto|\n")
    print("\t|2.- Salir         |\n")

def cartelera():
    print("\t|1.- El gato con botas 2 / Duracion: 1:23:44 / Hora : 11AM-13PM |\n")
    print("\t|2.- The joker  / Duracion: 1:36:00 / Hora : 14PM-16PM          |\n")

def ver(matriz):
    for fila in matriz:
        print(fila)

def promocion(dia,formato):
    if(dia in ["jueves","martes","JUEVES","MARTES"] and formato=="2d" ):
        return 5
    if(formato=="4d"):
        return 10
    else:
        return 7

def boletos(matriz):
    for fila in matriz:
            print(fila)
    asiento=int(input("El numero de fila que desea: \n"))
    while(asiento<=0 or asiento>=6):
        print("NO EXISTE ESE ASIENTO\n")
        asiento=int(input("El numero de fila que desea: \n"))
    asiento1=int(input("El numero de columna que desea: \n"))
    while(asiento1<=0 or asiento1>=6):
        print("NO EXISTE ESE ASIENTO\n")
        asiento1=int(input("El numero de columna que desea: \n"))
    matriz[asiento-1][asiento1-1]='x'
    for fila in matriz:
        print(fila)
    print("Asiento reservado\n")

def peliculaid(id):
    if(id==1):
        print("\t|1.- El gato con botas 2 / Duracion: 1:23:44 / Hora : 11AM-13PM |\n")
    if(id==2):
        print("\t|2.- The joker  / Duracion: 1:36:00 / Hora : 14PM-16PM          |\n")

def impresion(id,nombre,cedula,dia,formato):
    print("|----------------------------------------------\n")
    peliculaid(id)
    print(f"Nombre: {nombre}                               |")
    print(f"Nombre: {cedula}                               |")
    print(f"Nombre: {dia}                               |")
    print(f"Nombre: {formato}                               |")
    print(f"El costo del boleto es de: {promocion(dia,formato)} dolares")
    print("-------------------------------------------------\n")

def validardia(dia):
    while(dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="jueves" and dia!="viernes" and dia!="sabado" and dia!="domingo" ):
        print("DIA INCORRECTO\n")
        dia=input("Ingrese el dia que desea ver: \n")
    

matriz= [[0 for columna in range(5)] for fila in range (5)] 
while True:
    print("\t *****BIENVENIDO A SUPERSTAR***** \n")
    menu()
    opc=int(input("Elija una opcion : "))
    if(opc==1):
        print("")
        while True:
            print("|1= ver cartelera |\n |2= ver sala |\n|3= Comprar boleto |\n|4= Regresar |\n")
            opc=int(input("Que desea realizar: "))
            if(opc==1):
                cartelera()
            if(opc==2):
                cartelera()
                id=int(input("Ingrese el ID de la pelicula: "))
                peliculaid(id)
                print("\t-----Sala 1A-----\n")
                ver(matriz)
                print("\n")
            if(opc==3):
                id=int(input("Ingrese el ID de la pelicula: "))
                peliculaid(id)
                nombre=input("Ingrese su nombre: \n")
                cedula=int(input("Ingrese su numero de cedula: \n"))
                dia=input("Ingrese el dia que desea ver: \n")
                validardia(dia)
                formato=input("Desea ver en 2D o 3D o 4D : \n")
                while(formato !="2d" and formato!="3d" and formato!="4d"):
                    print("ERROR!! formato incorrecto ingrese una opcion valida :< \n")
                    formato=input("Desea ver en 2D o 3D : \n")
                #print(f"El costo del boleto es de: {promocion(dia,formato)}")
                boletos(matriz)
                impresion(id,nombre,cedula,dia,formato)
            if(opc==4):
                break
            else:
                print("OPCION INCORRECTA\n")
    if(opc==2):
        print("Gracias... por su compra vuelva pronto \n")
        break
    else:
        print("OPCION INCORRECTA\n")