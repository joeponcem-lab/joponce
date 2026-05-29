productos = {
    "Mouse": [10, 15000],
    "Teclado": [5, 25000],
    "Monitor": [3, 180000]
}
def agregar_producto(productos):
    nombre_produc=input("nombre del producto. ").strip()

    if nombre_produc == "":
        print("el nombre no puede estar vacio")
        return
    
    if nombre_produc in productos:
        print("el producto ya EXISTE")
        return

    stock=int(input("ingrese stock: "))
    precio=int(input("ingrese precio: "))

    productos[nombre_produc] = [stock,precio]
    print("PRODUCTO AGREGADO CON EXITO")





while True:
    print("---MENU---")
    print("1. AGREGAR PRODUCTOS\n2.MOSTRAR PRODUCTOS\n3.BUSCAR PRODUCTOS\n4.PRODUCTO MAS CARO\n5.SALIR")
    while True:
        try:
            op=int(input("seleccione una opcion"))
            break
        except ValueError:
            print("ERROR DEBES INGRESAR UN NUMERO DEL 1 AL 5, INTENTALO DENUEVO")

    """if op==1:
        agregar_producto(productos)
    elif op==2:
        ostrar_productos(productos)
    elif op==3:
        buscar_producto(productos)
    elif op==4:
        producto_mas_caro(productos)
    elif op ==5:
        print("FIN DEL PROGRESO")
        break
    else:
        print("OPCION INVALIDA")"""