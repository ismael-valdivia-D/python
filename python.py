
# # ##Diccionario con diccionarios
# # productosDicc={
# #    1:{"nombre": "Maracuyá", "precio": 3000},
# #    2:{"nombre": "Pera", "precio": 1500},
# #    3:{"nombre": "Cebolla", "precio": 1200}
# # }
# # carrito=[]
# # productosDicc[4]={"nombre": "Piña", "precio": 3500}
# # def agregarProducto():
# #    print("Cual es el nombre del producto?")
# #    nombre = input()
# #    print("cual es el precio?")
# #    precio = int(input())
# #    nuevoKey=list(productosDicc.keys())
# #    nuevoKey.sort()
# #    productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}
# # def MostrarProducto():
# #    for key, producto in productosDicc.items():
# #       print(f"{key} .-{producto}")
# # def eliminarProducto():
# #    MostrarProducto()
# #    try:
# #       borrar=int(input("Cual Producto borrará?: "))
# #       if borrar in productosDicc.keys():
# #          del productosDicc[borrar]
# #       else:
# #          print("Producto no existe")
# #    except Exception as e:
# #       print("Error:", e)
# # def actualizarProducto():
# #    MostrarProducto()
# #    num=int(input("Que producto desea actualizar?: "))
# #    if num in productosDicc.keys():
# #       nombre=input("Cual es el nombre nuevo?: ")
# #       precio=int(input("Cual es el precio nuevo?: "))
# #       productosDicc[num]={"nombre": nombre, "precio": precio}
# #    else:
# #       print("Producto no existe")

# # def comprar():
# #    while True:
# #       MostrarProducto()
# #       try:
# #          com=int(input("Que producto va a comprar?(0 para salir): "))
# #          if com==0:
# #             break
# #          if com in productosDicc.keys():
# #             carrito.append(productosDicc[com])
# #       except Exception as e:
# #          print("Error:", e)

# # def crearBoleta():
# #    total=0
# #    print("-"*30, "0", "-"*30)
# #    print("Bienvenido a minimarket Bender")
# #    for prod in carrito:
# #       print(f"{prod["nombre"]}___${prod["precio"]}")
# #       total+=prod["precio"]
# #    print("-"*30, "0", "-"*30)
# #    print(f"El total neto es{total} y el IVA es{total*0.19}")
# #    print(f"El total a pagar es{round(total*1.19)} ")
# #    print("Gracias por venir a minimarket Bender")
# #    print("-"*30, "0", "-"*30)
# # # print(productosDicc[2]["precio"])  # precio de la pera
# # # print(productosDicc[3]["nombre"])  # nombre de la cebolla

# # # for num, veg in productosDicc.items():
# # #     print(f"{num}.- {veg}")

# # ##Lista con diccionarios
# # productosList=[
# #    {"nombre": "Maracuyá", "precio": 3000}, #0
# #    {"nombre": "Pera", "precio": 1500},     #1  
# #    {"nombre": "Cebolla", "precio": 1200}   #2
# # ]

# # # print(productosList[2]["precio"]) #precio de la cebolla
# # # print(productosList[0]["nombre"]) #nombre de la naracuya



# # def vegetalesMenuDiccionario():
# #    while True:
# #       try:
# #          print("-"*20)
# #          print("1.- Agregar Vegetal")
# #          print("2.- Eliminar Vegetal")
# #          print("3.- Actualizar Vegetal")
# #          print("4.- Mostrar Vegetal")
# #          print("5.- Comprar")
# #          print("6.- Crear Boleta y Salir")
# #          op=int(input("Seleccione una opcion: "))
# #          match op:
# #                case 1:
# #                   agregarProducto()
# #                case 2:
# #                   eliminarProducto()
# #                case 3:
# #                   actualizarProducto()
# #                case 4:
# #                   MostrarProducto()
# #                case 5:
# #                   print("Comprar")
# #                   comprar()
# #                   print(carrito)
# #                case 6:
# #                   crearBoleta()
# #                   break
# #                case _:
# #                     print("Opcion invalida")  
# #       except Exception as e:
# #          print("Error:",e)
# # vegetalesMenuDiccionario()

# #Cambiar la funcion actualizar para que solo 
# # actualice una solo key 
# # Ademas, crear un CRUD pero con la lista 
# # de diccionarios.

             
             
             
# ## Crear un gestor de estacionamiento
# # Un estacionamiento tiene 4 pisos y cada piso tiene 20 estacionamientos.
# # Preguntar cuando entra un vehiculo, que tipo de vehiculo es
# # Vehiculo Ligero 2000
# # Vehiculo Mediano 3000
# # Vehiculo Pesado 3500

# # Luego, acomoda en algun lugar de algun piso disponible.
# # El menu debe tener las siguientes alternativas
# """
# 1.- Ingresa el vehiculo
# 2.- Contar Ganancias
# 3.- Contar Vehiculos
# """
# # Usa listas o diccionarios segun le acomode mas
                                                                                                                                  
# # TipoVehiculos = {
# #     1: {"tipo": "Vehiculo Ligero", "costo": 2000},
# #     2: {"tipo": "Vehiculo Mediano", "costo": 3000},
# #     3: {"tipo": "Vehiculo Pesado", "costo": 3500}
# # }

# # parking = {}
# # for piso in range(1, 5):
# #     for lugar in range(1, 21):
# #         parking[(piso, lugar)] = None


# # def MostarLVehiculos():
# #     print("Tipos de vehiculos:")
# #     for key in TipoVehiculos:
# #         info = TipoVehiculos[key]
# #         print(str(key) + ".- " + info["tipo"] + " - $" + str(info["costo"]))


# # def buscar_lugar():
# #     for piso in range(1, 5):
# #         for lugar in range(1, 21):
# #             if parking[(piso, lugar)] is None:
# #                 return piso, lugar
# #     return None, None


# # def EntradaVehiculos():
# #     MostarLVehiculos()
# #     try:
# #         entrada = int(input("Ingrese el tipo de vehiculo a ingresar: "))
# #     except ValueError:
# #         print("Debe ingresar un numero valido.")
# #         return

# #     if entrada != 1 and entrada != 2 and entrada != 3:
# #         print("Tipo de vehiculo invalido.")
# #         return

# #     piso, lugar = buscar_lugar()
# #     if piso is None:
# #         print("No hay espacios disponibles.")
# #         return

# #     parking[(piso, lugar)] = TipoVehiculos[entrada]
# #     print("Vehiculo ingresado en piso " + str(piso) + ", lugar " + str(lugar) + ".")


# # def ContarGanancias():
# #     total = 0
# #     for piso in range(1, 5):
# #         for lugar in range(1, 21):
# #             if parking[(piso, lugar)] is not None:
# #                 total = total + parking[(piso, lugar)]["costo"]
# #     return total


# # def ContarVehiculos():
# #     cantidad = 0
# #     for piso in range(1, 5):
# #         for lugar in range(1, 21):
# #             if parking[(piso, lugar)] is not None:
# #                 cantidad = cantidad + 1
# #     return cantidad


# # def MenuVehiculos():
# #     while True:
# #         print("1.- Ingresa el vehiculo")
# #         print("2.- Contar Ganancias")
# #         print("3.- Contar Vehiculos")
# #         print("4.- Salir")
# #         try:
# #             op = int(input("Ingrese el numero de la opcion deseada: "))
# #         except ValueError:
# #             print("Error: ingrese un numero valido")
# #             continue

# #         if op == 1:
# #             EntradaVehiculos()
# #         elif op == 2:
# #             print("Ganancias totales: " + str(ContarGanancias()))
# #         elif op == 3:
# #             print("Cantidad de vehiculos: " + str(ContarVehiculos()))
# #         elif op == 4:
# #             print("Saliendo del programa.")
# #             break
# #         else:
# #             print("Opcion invalida, intente nuevamente.")




# # MenuVehiculos()
         



    
# ## Crear un gestor de pacientes

# pacientes=[
#     {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
#      "temperatura":34.6, "grave": False}
# ]

# '''crear al gestor de pacientes en un centro medico
# Para poner el nombre se debe validar que no este vacio 
# y ademas tenga mas de 8 caracteres
# Para la prevision de salud solo exiten 3 posibles valores
# Fonasa, Isapre, o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no
# Para que este grave debe tener mas de 39°
# Cada atencion vale $25.000
# Los despcuentos corresponden a 
# FOnasa 54%
# Isapre 27%
# Fodesa 12,5%

# '''

# def validarEstado(tempe):
#    if tempe>39:
#        return True 
#    else:
#        return False
# def mostrarPacientes():
#     if len(pacientes)==0:
#         print("No hay pacientes")
#     else:
#         c=1
#         for p in pacientes:
#             print(f"{c} .- {p}")
#             c+=1
# while True:
#     try:
#         print("1.- Ingresar paciente")
#         print("2.- Quitar paciente")
#         print("3.- Tomar Temperatura")
#         print("4.- Cobra atencion")
#         print("5.- Mostrar Pacientes")
#         print("9.- Salir")
#         op=int(input("Ingrese una opcion: "))
#         match op:
#             case 1:
#                 nombre=input("Ingrese nombre: ")
#                 prevision=input("Ingrese prevision: ")
#                 temp=float(input("Ingrese temp: "))
#                 pacientes.append({"nombre": nombre, "prevision": prevision, 
#                             "temperatura":temp, "grave": validarEstado(temp)})
#                 print("Paciente agregado al listado")
#             case 2:
#                 mostrarPacientes()
#                 paci=int(input("Que paciente se vá?: "))
#                 pacientes.pop(paci-1)
#                 print("Paciente eliminado.")
#             case 3:
#                 print("")
#             case 4:
#                 print("")
#             case 5:
#                 mostrarPacientes()
#             case 9:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opción inválida")
#     except Exception as e:
#         print("Error:" , e)


