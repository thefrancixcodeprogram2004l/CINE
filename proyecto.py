
'''
en def menu creamos una funcion para visualizar el menu
'''

def menu():
    print("\t|1.- Menu de inicio de superstar|\n") 
    print("\t|2.- Salir                      |\n")

'''
en def cartelera ponemos los datos de las peliculas
'''

def cartelera():
    print("\t|1.- El gato con botas 2 / Duracion: 1:23:44 / Hora : 11AM-13PM |\n")
    print("\t|2.- The joker  / Duracion: 1:36:00 / Hora : 14PM-16PM          |\n")
    print("\t|3.- The Avatar / Duracion: 1:16:40 / Hora : 16PM-18PM          |\n")
    print("\t|4.- Thor love  / Duracion: 0:98:23 / Hora : 18PM-20PM          |\n")

'''
en def ver visualizamos la matriz
'''

def ver(matriz):
    for fila in matriz:
        print(fila)

'''
en def promocion mandamos como parametros el dia y el formato para
que me retorne el valor del boleto
'''
def promocion(dia,formato):
    if(dia in ["jueves","martes","JUEVES","MARTES"] and formato=="2d" ):
        return 5
    if(formato=="4d"):
        return 10
    else:
        return 7

'''
en def boletos mandamos como parametros la matriz para que cada 
que selecione un asiento se marce con una 'x' para 
reservarlo y guardar el resultado
'''
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
    matriz[asiento-1][asiento1-1]='x' # esta parte del codigo hace el cambio de 0 a 'x'
    for fila in matriz:
        print(fila)
    print("Asiento reservado\n")

'''
en def pelicula id mandamos como parametros el id para poder ver 
que peliculas compramos es una funcion para poder llamarla en la parte del codigo que 
necesitemos como ver cartelera y compra
'''
def peliculaid(id):
    if(id==1):
        print("\t|1.- El gato con botas 2 / Duracion: 1:23:44 / Hora : 11AM-13PM |\n")
    if(id==2):
        print("\t|2.- The joker  / Duracion: 1:36:00 / Hora : 14PM-16PM          |\n")
    if(id==3):
        print("\t|3.- The Avatar / Duracion: 1:16:40 / Hora : 16PM-18PM          |\n")
    if(id==4):
        print("\t|4.- Thor love  / Duracion: 0:98:23 / Hora : 18PM-20PM          |\n")
    else:
        while(id<0 or id>4):
            print("Ingrese un id valido :< \n")
            id=int(input("Ingrese el ID de la pelicula: "))

'''
en def promocion1 mandamos como parametros el dia y el formato para
que me retorne un string si esta con promocion de 2x1 
el dia que va a comprar
'''
def promocion1(dia,formato):
    if(dia in ["jueves","martes","JUEVES","MARTES"] and formato=="2d" ):
        return ("Promocion de dia 2x1 ")
    if(formato=="4d"):
        return (" ")
    else:
        return (" ")
'''
en def impresion mandamos como parametros todos
los datos obtenidos anteriormente para hacer la impresion
del boleto
'''
def impresion(id,nombre,cedula,dia,formato):
    print("|----------------------------------------------|\n")
    peliculaid(id)
    print(f"Nombre: {nombre}                                           |")
    print(f"Cedula: {cedula}                                           |")
    print(f"Dia: {dia} / {promocion1(dia,formato)}                     |")
    print(f"Formato: {formato}|")
    print(f"El costo del boleto es de: {promocion(dia,formato)} dolares|")
    print("|-------------------------------------------------|\n")
'''
en def validardia verificamos que el usuario
ingrese un dia correcto 
'''
def validardia(dia):
    while(dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="jueves" and dia!="viernes" and dia!="sabado" and dia!="domingo" ):
        print("DIA INCORRECTO\n")
        dia=input("Ingrese el dia que desea ver: \n")

'''
en def confirmacion validamos que la compra sea realizada con exito
'''

def confirmacion (conf,suma):
    while(conf!="si" and conf!="SI" and conf!="no" and conf!="NO"):
        print("ERROR!!")
        conf=input("Desea para confirmar su compra aceptar/cancelar \n")
    if(conf=="si" or conf=="SI"):
        print(f"EL COSTO TOTAL DE SU COMPRA ES DE: {suma} $")
        print("\t !GRACIAS POR SU COMPRA¡\t\n")
    else:
        print(("\t !GRACIAS POR VISITARNOS¡\t\n"))

matriz= [[0 for columna in range(5)] for fila in range (5)] #creamos una matriz llena de ceros
suma=0 
while True:
    print("\t *****BIENVENIDO A SUPERSTAR***** \n")
    menu() #llamamos ala funcion menu
    opc=int(input("Elija una opcion : "))
    if(opc==1):
        print("")
        while True:
            print("|1= ver cartelera |\n|2= ver sala |\n|3= Comprar boleto |\n|4= Regresar |\n") #una manera diferente de crear un menu
            opc=int(input("Que desea realizar: "))
            while(opc<0 or opc>4): #validacion de datos
                print("Ingrese una opcion valida :) \n")
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
                a=int(input("Cuantos boletos desea comprar: \n"))
                while(a<1):
                    a=int(input("Cuantos boletos desea comprar: \n"))
                for i in range (a):
                    boletos(matriz)
                    impresion(id,nombre,cedula,dia,formato)
                    suma+=promocion(dia,formato)
                conf=input("Desea para confirmar su compra aceptar/cancelar \n")
                confirmacion(conf,suma)         
            if(opc==4):
                break #rompemos el while true
    if(opc==2):
        print("Gracias... por su compra vuelva pronto \n")
        break
    else:
        print("OPCION INCORRECTA\n") 