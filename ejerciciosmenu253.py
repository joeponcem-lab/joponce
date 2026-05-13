deuda=100000
saldo=400000


menu = True
while menu:
    print("MENU")
    print("1-pago credito")
    print("2-suimulacion de pago")
    print("3-salir")
    while True:
        try:
            op=int(input("inrese su opcion: "))
            break
        except ValueError:
            print("Error, El valor debe ser numerico entre 1 y 3,intente nuevamente")

    if op==1:
        print("pago tarjeta de credito")
        print(f"deuda:${deuda}")
        while True:
            try:
                pago=int(input("ingrese un monto de pago: "))
                break
            except ValueError:
                print("Error, El valor debe ser numerico")
        if pago>=0:
            if pago<=deuda:
                deuda=deuda-pago
                saldo=saldo+pago
                print(f"pago exitoso! su nueva deuda es ${deuda}")   
            else:
                print("el pago excede la deuda")
    elif op ==2:
        print("comprando")
        print(f"su saldo para comprar es: ${saldo}")
        cont=0
        
        for i in range (saldo):
            cont=cont+1
            print("compra: ",cont)
            Montocompra=int(input("ingrese monto de compra: $ "))

            if Montocompra>=0:
                if saldo>=Montocompra:
                    saldo=saldo-Montocompra
                    deuda=deuda+Montocompra
                    print(f"Su saldo es: {saldo}")
                    if Montocompra==0 or saldo<=0:
                        break
                else:
                    print("saldo insuficiente")
                    break
            else:
                print("pofavor ingrese valor mayor que cero")

    elif op==3:
        print("saliendo")
        menu = False
    else:
        print("opcion no valida")