lista_tareas=[

]

def agregar_tarea():
    nueva_tarea=input("escribe la tarea que quieras agregar: ")
    lista_tareas.append(nueva_tarea)
    print(f"{nueva_tarea},agregada con exito")

def eliminar_tarea():
    if len(lista_tareas)==0:
        print("no ahi tareas pendientes")
    else:
        tarea_eliminar=input("escribe el nombre excato de la tarea que quieras eliminar: ")
        if tarea_eliminar in lista_tareas:
            lista_tareas.remove(tarea_eliminar)
            print(f"{tarea_eliminar},ha sido elimindada")
        else:
            print("esa tarea no se encuentra en la lista")

def imprimir_tareas(lista_tareas):
    if len(lista_tareas) ==0:
        print("no ahi tareas pendientes")
    else:
        lista_tareas.sort()
        for tarea in lista_tareas:
            print(tarea)

def mostrarmenu():
    print("1-agregar tarea\n2-eliminar tarea\n3-ver tarea ordenadas\n4-salir")


while True:
    mostrarmenu()
    while True:
        try:
            op=int(input("ingrese una opcion: "))
            break
        except ValueError:
            print("ingrese una opcion valida")

    if op ==1:
       agregar_tarea()
    elif op==2:
       eliminar_tarea()
    elif op ==3:
        print("tus tareas ordenadas: ")
        imprimir_tareas(lista_tareas)
    elif op ==4:
        print("saliendo del programa...")
        break
    else:
        print("opcion invalida")
