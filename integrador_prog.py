from funciones import crear_aventura, guardar_arbol, cargar_aventura, jugar, elegir_aventura, preorden, inorden, postorden, mostrar_menu, elegir_opción, limpiar_pantalla

submenu_ver_aventura = ["--- Ver aventura ---","1. Recorrido Preorden","2. Recorrido Inorden","3. Recorrido Postorden","0. Volver al menú principal"]
menu_principal = ["--- MENU ---","1. Crear aventura nueva","2. Jugar aventura","3. Ver aventura","4. Salir"]

VIDAS_MAXIMAS = 3

def menu_ver_aventura():
    nombre_aventura = elegir_aventura()
    aventura = cargar_aventura(nombre_aventura)

    while True:
        mostrar_menu(submenu_ver_aventura)
        opcion = elegir_opción("Elegí una opción:")

        if opcion == '1':
            recorrido = preorden(aventura)
            print("\nRecorrido Preorden:")
            for paso in recorrido:
                print(f"- {paso}")
        elif opcion == '2':
            recorrido = inorden(aventura)
            print("\nRecorrido Inorden:")
            for paso in recorrido:
                print(f"- {paso}")
        elif opcion == '3':
            recorrido = postorden(aventura)
            print("\nRecorrido Postorden:")
            for paso in recorrido:
                print(f"- {paso}")
        elif opcion == '0':
            break
        else:
            print("Opción inválida, probá de nuevo.")

# # Función del menu
def menu():
    while True:
        mostrar_menu(menu_principal)
        opcion = elegir_opción("Elegí una opción:")
        if opcion == '1':
            # # Crea una lista de la nueva aventura
            arbol = crear_aventura()
            while True:
                # # asigna un nombre para guardar el archivo
                nombre = input("Ingresá el nombre del archivo para guardar (ej: mi_aventura): ").strip()
                if nombre:
                    if not nombre.endswith(".json"):
                        nombre += ".json"
                    guardar_arbol(arbol, nombre)
                    break
                else:
                    print("El nombre no puede estar vacío.")
        elif opcion == '2':
            nombre_aventura = elegir_aventura()
            if nombre_aventura:
                aventura = cargar_aventura(nombre_aventura)
                jugar(aventura, VIDAS_MAXIMAS, aventura)
            else:
                continue
        elif opcion == '3':
            menu_ver_aventura()
        elif opcion == '4':
            print("Gracias por jugar!")
            break
        else:
            print("Opción inválida. Probá de nuevo.")

# # Programa principal
if __name__ == "__main__":
    limpiar_pantalla()
    menu()
