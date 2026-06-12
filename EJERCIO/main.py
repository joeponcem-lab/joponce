import funciones as fn 

catalogo= [
    {"titulo": "Elden Ring", "precio": 45499},
    {"titulo": "Cyberpunk 2077", "precio": 39999},
    {"titulo": "Stardew Valley", "precio": 7500},
    {"titulo": "Hollow Knight", "precio": 8300},
    {"titulo": "Sekiro: Shadows Die Twice", "precio": 47650},
    {"titulo": "Resident Evil 4", "precio": 27600},
    {"titulo": "Dead by Daylight", "precio": 11994},
    {"titulo": "Clair Obscur: Expedition 33", "precio": 39990},
    {"titulo": "Project Zomboid", "precio": 10500},
    {"titulo": "Backrooms: Escape Together", "precio": 5750},
    {"titulo": "Lethal Company", "precio": 5750},
    {"titulo": "Helldivers 2", "precio": 28000},
    {"titulo": "Red Dead Redemption 2", "precio": 35948},
    {"titulo": "God of War", "precio": 35000}
]

carrito_compras= []
biblioteca_juegos= []


nombre_jugador=input("Bienvenido a steam ingrese tu nombre de jugador\n==> ")
saldo_cartera = 0

while True:
    fn.mostrar_menu()
    while True:
        try:
            opcion=int(input(f"[{nombre_jugador} | Saldo: ${saldo_cartera}] Selecciona una opción\n==> "))
            break
        except ValueError:
            print("error: Por favor, ingresa solo el número de la opción (un entero del 1 al 7).")

    if opcion==1:
        print("---CATALOGO DE LA TIENDA---")
        fn.mostrar_juegos(catalogo)
    elif opcion==2:
        nombre_buscar=input("ingresa el nombre del juego que buscar\n:")
        juego_encontrado=fn.buscar_juego(catalogo,nombre_buscar)
        if juego_encontrado is not None:
            if juego_encontrado in carrito_compras:
                print(f"El juego '{juego_encontrado['titulo']}' ya está en tu carrito.")
            elif juego_encontrado in biblioteca_juegos:
                print(f"Ya eres dueño de '{juego_encontrado['titulo']}'. ¡Revisa tu biblioteca!")
            else:
                carrito_compras.append(juego_encontrado)
                print(f"¡'{juego_encontrado['titulo']}' ha sido agregado al carrito con éxito!")
        else:
            print("Lo sentimos, ese juego no se encuentra en el catálogo")
    elif opcion==3:
        print("---TU CARRITO DE COMPRAS---")
        fn.mostrar_juegos(carrito_compras)
        total_pagar=fn.calcular_total(carrito_compras)
        print(f"Total actual a pagar: ${total_pagar}")
    elif opcion==4:
        try:
            monto=int(input("cuanto dinero quiere ingresar\n$:"))
            if monto > 0:
                saldo_cartera+= monto
                print(f"¡Carga exitosa! Tu nuevo saldo es: ${saldo_cartera}")
            else:
                print("Error: El monto a cargar debe ser mayor a $0.")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
    elif opcion==5:
        if len(carrito_compras)==0:
            print("Tu carrito está vacío. No hay nada que pagar.")
        else:
            total_compra=fn.calcular_total(carrito_compras)

            if saldo_cartera>= total_compra:
                saldo_cartera -= total_compra
                biblioteca_juegos.extend(carrito_compras)
                carrito_compras.clear()
                print("¡Compra realizada con éxito! Los juegos se han añadido a tu biblioteca.")
            else:
                pesos_faltantes = total_compra - saldo_cartera
                print(f"Fondos insuficientes. Te faltan ${pesos_faltantes} para completar la compra.")
    elif opcion==6:
        print("---TU BIBLIOTECA DE JUEGOS---")
        fn.mostrar_juegos(biblioteca_juegos)
    elif opcion==7:
        print("gracias por usar nuestro simulador")
        break
    else:
        print("opcion invalida")