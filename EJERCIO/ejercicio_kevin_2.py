def opcion():
    op=input("[A] Agregar contacto | [B] Buscar | [S] Salir: ")
    return op.upper()

def buscar_numero(agenda,nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        return "el contacto no existe"
    
contactos={}
"""def buscar_numero(agenda, nombre_buscado):
    # Revisamos si el nombre está en las llaves del diccionario
    if nombre_buscado in agenda:
        return agenda[nombre_buscado]  # Retorna el teléfono si existe
    else:
        return "El contacto no existe."  # Mensaje si no existe


# ==========================================
# 3. Lógica Principal
# ==========================================
# Creamos el diccionario vacío tal como lo pide la guía
contactos = {}

# Iniciamos el bucle interactivo
while True:
    # Guardamos en una variable lo que retorna pedir_opcion()
    eleccion = pedir_opcion()
    
    # Si elige salir, rompemos el bucle while
    if eleccion == "S":
        print("¡Hasta luego!")
        break
        
    # Si elige "A": Agregar contacto
    elif eleccion == "A":
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono: ")
        # Guardamos en el diccionario -> contactos[llave] = valor
        contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado con éxito.")
        
    # Si elige "B": Buscar contacto
    elif eleccion == "B":
        nombre_a_buscar = input("Ingresa el nombre a buscar: ")
        # Llamamos a la función pasándole el diccionario y el nombre
        resultado = buscar_numero(contactos, nombre_a_buscar)
        # Imprimimos lo que la función nos devuelva
        print(resultado)
        
    # Por si ingresa cualquier otra letra
    else:
        print("Opción no válida. Intenta de nuevo.")
    
    print("-" * 30)  # Una línea para separar cada vuelta del menú"""