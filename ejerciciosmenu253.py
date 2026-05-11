menu = True
while menu:
    print("MENU")
    print("1-pago credito")
    print("2-suimulacion de pago")
    print("3-salir")

    op=int(input("inrese su opcion"))

    if op==1:
        print("pago tarjeta de credito")
    elif op ==2:
        print("comprando")
    elif op==3:
        print("saliendo")
        menu = False
    else:
        print("opcion no valida")