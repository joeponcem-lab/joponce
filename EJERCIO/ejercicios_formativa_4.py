usuario_registrados={


}

def main():
    print("1.- Ingresar usuario.\n2.- Buscar usuario.\n3.- Eliminar usuario.\n4.- Salir.")

def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ").strip()
        
        repetido = False
        for usuario in usuario_registrados:
            if usuario["nombre"] == nombre:
                repetido = True
                break
        
        if repetido:
            print("el nombre de usuario ya existe. Intenta con otro.")
        else:
            break 

    while True:
        sexo = input("Ingrese sexo (F/M): ").strip().upper()
        if sexo in ["F", "M"]:
            break
        print("el sexo debe ser 'F' o 'M'. Inténtalo de nuevo")

    while True:
        contrasena = input("Ingrese contraseña: ")
        valida = True
        if len(contrasena) < 8:
            print("debe tener un largo mínimo de 8 caracteres.")
            valida = False
            
        if " " in contrasena:
            print("no puede contener espacios en blanco.")
            valida = False
            
        tiene_numero = False
        tiene_letra = False
        for caracter in contrasena:
            if caracter.isdigit():
                tiene_numero = True
            if caracter.isalpha():
                tiene_letra = True
                
        if not tiene_letra or not tiene_numero:
            print("debe tener al menos 1 letra y al menos 1 número.")
            valida = False
            
        if valida:
            break 
        else:
            print("inténtalo de nuevo.")

    usuario_registrados[nombre]=[sexo,contrasena]
    
    print("el usuario ha sido ingresado exitosamente")
    return True

def buscar_usuario():
    nombre_buscar=input("ingrese exactamente el nombre que quieres buscar: ").strip()
    for usuario in usuario_registrados:
        if usuario== nombre_buscar:
            print("Usuario encontrado!")
            print(f"Sexo: {usuario}")
            print(f"Contraseña: {usuario}")
            return True
        else:
            print("el usuario no se encuentra.")
            return False
        
def borrar_usuario():
    nombre_borrar=input("ingrese el nombre a eliminar: ").strip()
    for usuario in usuario_registrados:
        if usuario == nombre_borrar:
            usuario_registrados.remove(usuario)
            print("usuario eliminado")
            return True
        else:
            print("no se pudo eliminar usuario! (no se encuentra)")
            return False
        
def salir_menu():
    print("gracias por utilizarnos.")
    menu=False



menu =True
while menu:
    main()
    while True:
        try:
            op=int(input("ingrese una opcion: "))
            break
        except ValueError:
            print("ingrese una opcion valida")
        
    if op ==1:
        ingresar_usuario()
    elif op ==2:
        buscar_usuario()
        print(usuario_registrados)
    elif op ==3:
        borrar_usuario()
    elif op ==4:
        salir_menu()
    else:
        print("opcion invalida")