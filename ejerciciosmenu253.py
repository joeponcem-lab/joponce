deuda=100000

menu = True
while menu:
    print("MENU")
    print("1-pago credito")
    print("2-suimulacion de pago")
    print("3-salir")

    op=int(input("inrese su opcion"))

    if op==1:
        print("pago tarjeta de credito")
        pago=int(input("ingrese un monto de pago"))
        if pago>=0:
            if pago<=deuda:
                deuda=deuda-pago
                print(f"pago exitoso! su nueva deuda es ${deuda}")
            else:
                print("el ago excede la deuda")
    elif op ==2:
        print("comprando")
    elif op==3:
        print("saliendo")
        menu = False
    else:
        print("opcion no valida")