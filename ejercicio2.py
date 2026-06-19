# notas=[4.6, 7.0,3.4,6.6 , 3.9, 6.8]

# # crear un a funcion para poder pasarle la lista
# # como parametro y msotrar el promedio
# # mostrar si aprueba o reprueba


# print(max(notas))
# print(min(notas))















peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "anio": 2010, "rate": 8.9 },
    {"titulo": "Jurassic Park", "director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "anio": 1993 , "rate": 9.6},
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thiller", "anio": 1997 , "rate": 9.3},
]
# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
'''1.- ingresar Pelicula
2.- quitar Pelicula
3.- Actualizar Pelicula
4.- Mostar Peliculas
5.- Mostrar solo los titulos
6.- Mostrar los aos de las peliculas ordenados
7.- Mostrar meplicula mejor calificada
9.- Salir
'''





aniospelis = [peli["anio"] for peli in peliculas]
def MostrarAniosPeli():
         if len(aniospelis)==0:
            print("No hay pacientes")
         else:
            c=1
            for p in aniospelis:
                print(f"{c} .- {p}")
                c+=1

def ingresarPelicula():
                titulo=input("Ingrese el titulo de su pelicula: ")
                director=input("Ingrese el Director de su pelicula: ")
                genero=input("Ingrese el genero de su pelicula")
                anio=int(input("Ingrese el anio de su pelicula"))
                rate=int(input("Ingrese el rate de su pelicula"))
                peliculas.append({"titulo": titulo, "director": director, 
                "genero":genero, "anio": anio, "rate":rate})
                print("Pelicula agregada correctamente al listado")

def QuitarPelicula():
    mostrarPeliculas()
    borrar=int(input("cual pelicula desea retirar?(Ingresar numero): "))
    peliculas.pop(borrar-1)

def mostrarPeliculas():
    if len(peliculas)==0:
        print("No hay peliculas")
    else:
        c=1
        for p in peliculas:
            print(f"{c} .- {p}")
            c+=1

def actualizarpelicula():
   mostrarPeliculas()
   num=int(input("Que Pelicula desea actualizar?: "))
   if num in peliculas.keys():
    titulo=input("Ingrese el titulo de su pelicula: ")
    director=input("Ingrese el Director de su pelicula: ")
    genero=input("Ingrese el genero de su pelicula")
    anio=int(input("Ingrese el anio de su pelicula"))
    rate=int(input("Ingrese el rate de su pelicula"))
    peliculas[num]={"titulo": titulo, "director": director, 
    "genero":genero, "anio": anio, "rate":rate}
   else:
      print("Pelicula no existe")

def mostrarMejorCalificada():
    if len(peliculas) == 0:
        print("No hay películas registradas.")
    else:
        print(max(peliculas, key=lambda peli: peli["rate"]))

while True:
    try:
        print("1.- Ingresar Pelicula")
        print("2.- Quitar Pelicula")
        print("3.- Actualizar Pelicula")
        print("4.- Mostrar Peliculas")
        print("5.- Mostrar Solo Titulos")
        print("6.- Mostrar ls anios de las peliculas ordenados")
        print("7.- Mostrar pelicula mejor clasificada")
        print("9.-Salir")
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                ingresarPelicula()

            case 2:
                QuitarPelicula()
                print("Pelicula retirada")

            case 3:
                  actualizarpelicula()
            
            case 4:
                mostrarPeliculas()

            case 5:
                for p in peliculas:
                    print(p({"titulo"}))

            case 6:
                MostrarAniosPeli()

            case 7:
                mostrarMejorCalificada()

            case 9:
                print("Saliendo")
                break
            case _:
                print("Opción inválida")
    except Exception as e:
        print("Error:" , e)



                







