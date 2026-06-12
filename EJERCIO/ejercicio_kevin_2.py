contactos={}

def pedir_opcion():
    op=input("[A]agregar contacto | [B] buscar contacto| [C]salir")
    return op

def buscar_numero(agenda,nombre_buscado):
    if nombre_buscado in agenda:
        return agenda[nombre_buscado]
    else:
        return "eel contacto no existe en la agenda"
    
while True:
    opcion = pedir_opcion()

    if opcion=="A":
        nombre =input("ingrese el nombre").strip().title()
        numero=input("Ingreso el telefono").strip().title()

        contactos[nombre] = numero
        print(f"contacto {nombre} guardado")

    elif opcion=="B":
        nombre=input("buscando contacto: ").strip().title()

        resultado=buscar_numero(contactos,nombre)
        print(f"Resultado: {resultado}")
    elif opcion=="C":
        print("Saliendo")
        break
    else:
        print("opcion invalida")