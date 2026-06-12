def mostrar_menu():
    print("\n--- SIMULADOR DE STEAM ---")
    print("1. Ver Catálogo de Tienda")
    print("2. Agregar juego al Carrito")
    print("3. Ver mi Carrito")
    print("4. Cargar fondos a la Cartera")
    print("5. Pagar Carrito")
    print("6. Ver mi Biblioteca")
    print("7. Salir")

def mostrar_juegos(lista_generica):
    if len(lista_generica)==0:
        print("no ahi juegos para mostrar.")
    else:
        for juego in lista_generica:
            print(f"- {juego['titulo']} | Precio: ${juego['precio']}")

def calcular_total(lista_generica):
    total=0
    for juego in lista_generica:
        total+=juego['precio']
    return total

def buscar_juego(catalogo,nombre_buscado):
    for juego in catalogo:
        if juego['titulo'].lower()==nombre_buscado.lower():
            return juego
    return None
