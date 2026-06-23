#poner una propiedad mas en cada pintura
#el nuevo key es cantidad
#al ingresar una pintura nueva la cantidad es 0 

pinturas = [
    {"color": "verde", "capacidad": 1500, "formato": "tarro"   , "cantidad" : 76}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"    , "cantidad" : 15}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja" , "cantidad" : 12}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"  , "cantidad" : 10}, #3
]

def mostrarPinturas():
    if len(pinturas)<1:
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.- {p}")
            c+=1

def quitarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a eliminar?: "))
    pinturas.pop(ele-1)

def agregarPintura():
    color=input("Que color será?: ")
    capacidad=int(input("Que capacidad será?: "))
    formato=input("Que formato será?: ")
    pinturas.append({"color": color, "capacidad": capacidad, "formato": formato, "cantidad": 0})

def actualizarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a actulizar?: "))
    print("1.- Color")
    print("2.- Capacidad")
    print("3.- Formato")
    dato=int(input("Que dato de la pintura va a actulizar?: "))
    nuevoValor=input
    if dato==1:
        nuevoValor=input("Ingrese el nuevo color")
        pinturas[ele-1]["color"]=nuevoValor
    elif dato==2:
        nuevoValor=int(input("Ingrese la nueva capaciadad"))
        pinturas[ele-1]["capacidad"]=nuevoValor
    elif dato==3:
        nuevoValor=input("Ingrese el nuevo formato")
        pinturas[ele-1]["formato"]=nuevoValor
    else:
        print("Dato invalido")

def mayorCap():
    listaCapacidad=[]
    for p in lista:
        listaCapacidad.append(p["capacidad"])
    return max(listaCapacidad)

def validarContabilidad():
    for p in pinturas:
        # Usamos .get() por seguridad por si alguna pintura no tiene la clave 'cantidad'
        stock = p.get("cantidad", 0)
        
        if stock < 20:
            print(f"Pintura {p['color']}: Estado crítico")
            p["cantidad"] = stock + 20  # Agrega las 20 unidades al stock real
        else:
            print(f"Pintura {p['color']}: Stock razonable")


def stockPinturas(pinturas):

    for p in pinturas:
        stock=p["cantidad"]
        if stock < 20 :
            p["cantidad"] = stock + 15
            print("Stock Critico")
        else:
            print("Stock Razonable")

def menuPinturas():    
    while True:
        try:
            print("-"*60)
            print("1.- Agregar Pintura")
            print("2.- Quitar Pintura")
            print("3.- Actualizar Pintura")
            print("4.- Mostrar Pinturas")
            print("5.- Mostrar mayor capacidad")
            print("6._Validar stock")
            print("9.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregarPintura()
                case 2:
                    quitarPintura()
                case 3:
                    actualizarPintura()
                case 4:
                    mostrarPinturas()  
                case 5:
                    print(f"El recipiente con mayor capacidad tine : {mayorCap(pinturas)}")  
                case 6:
                    stockPinturas(pinturas)
                case 9:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion invalida")
        except Exception as e:
            print("error: ", e)
    
menuPinturas()