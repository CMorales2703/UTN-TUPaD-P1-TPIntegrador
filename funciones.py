import json
import os

CARPETA_AVENTURAS = "aventuras"

# # manejo de archivos
def cargar_aventura(nombre_archivo):
    ruta_completa = os.path.join(CARPETA_AVENTURAS, nombre_archivo)
    with open(ruta_completa, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_arbol(arbol, nombre_archivo):
    ruta_completa = os.path.join(CARPETA_AVENTURAS, nombre_archivo)
    with open(ruta_completa, "w", encoding="utf-8") as f:
        json.dump(arbol, f, indent=2, ensure_ascii=False)
    print(f"¡Aventura guardada en {ruta_completa}!")

def listar_aventuras():
    return [f for f in os.listdir(CARPETA_AVENTURAS) if f.endswith(".json")]

# # limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# # validación de nodo
def es_hoja(nodo):
    return len(nodo) == 2 and isinstance(nodo[1], bool)

# # creación de aventura
def crear_aventura(ruta="raíz"):
    print(f"\n📍 Estás creando el nodo en la posición: {ruta}")

    while True:
        es_final = input("¿Este nodo es un final? (s/n): ").strip().lower()
        if es_final in ['s', 'n']:
            break
        print("Respuesta inválida. Usá 's' o 'n'.")
    
    if es_final == 's':
        while True:
            mensaje = input("Ingresá el mensaje final: ").strip()
            if mensaje:
                break
            print("El mensaje no puede estar vacío.")
        while True:
            malo = input("¿Es un final malo? (pierde vida) (s/n): ").strip().lower()
            if malo in ['s', 'n']:
                final_malo = (malo == 's')
                break
            print("Respuesta inválida. Usá 's' o 'n'.")
        return [mensaje, final_malo]
    else:
        while True:
            pregunta = input("Ingresá el texto de la pregunta para este nodo: ").strip()
            if pregunta:
                break
            print("La pregunta no puede estar vacía.")

        print(f"\n🌿 Creando hijo IZQUIERDO de: '{pregunta}'")
        hijo_izq = crear_aventura(ruta + " -> izquierda")

        print(f"\n🌿 Creando hijo DERECHO de: '{pregunta}'")
        hijo_der = crear_aventura(ruta + " -> derecha")

        return [pregunta, hijo_izq, hijo_der]

def elegir_aventura():
    aventuras_disponibles = listar_aventuras()
    if not aventuras_disponibles:
        print("No hay aventuras guardadas. Primero creá una.")
        return None
    mostrar_menu(construir_menu_aventuras(aventuras_disponibles))
    
    while True:
        entrada = elegir_opción("Elegí una aventura (número):")
        
        if not entrada.isdigit():
            print("Opción inválida. Ingresá un número.")
            continue

        opcion = int(entrada)
        
        if opcion == 0:
            return None  # Volver al menú
        if 1 <= opcion <= len(aventuras_disponibles):
            return aventuras_disponibles[opcion - 1]
        
        print("Opción inválida.")


def jugar(nodo, vidas, aventura):
    if es_hoja(nodo):
        mensaje, final_malo = nodo
        print("\n" + mensaje)
        if final_malo:
            vidas -= 1
            print(f"Te quedan {vidas} vidas.\n")
            if vidas <= 0:
                print("¡Game over! ☠️")
                return
            else:
                jugar(aventura, vidas, aventura)
        else:
            print("¡Juego terminado con éxito! 🏆")
        return

    pregunta = nodo[0]
    izq = nodo[1]
    der = nodo[2]

    print("\n" + pregunta)
    eleccion = elegir_opción("Elegí (i/d):").strip().lower()

    if eleccion == 'i':
        jugar(izq, vidas, aventura)
    elif eleccion == 'd':
        jugar(der, vidas, aventura)
    else:
        print("Opción inválida. Probá de nuevo.")
        jugar(nodo, vidas, aventura)

# # Menus
def construir_menu_aventuras(aventuras_disponibles):
    menu = ["--- Aventuras disponibles ---"]
    for i, nombre in enumerate(aventuras_disponibles):
        menu.append(f"{i + 1}. {nombre}")
    menu.append("0. Volver al menú principal")
    return menu

def elegir_opción(mensaje):
    opcion = input(f"\n{mensaje} ").strip()
    
    return opcion

def mostrar_menu(menu):
    for i in range(len(menu)):
        if i == 0:
            print(f"\n{menu[i]}")
        else:
            print(menu[i])

        if i == len(menu) - 2:
            print("-" * len(menu[0]))

# # Orden
def preorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo is None:
        return resultado
    if es_hoja(nodo):
        resultado.append(nodo[0])
    else:
        resultado.append(nodo[0])
        preorden(nodo[1], resultado)
        preorden(nodo[2], resultado)
    return resultado

def inorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo is None:
        return resultado
    if es_hoja(nodo):
        resultado.append(nodo[0])
    else:
        inorden(nodo[1], resultado)
        resultado.append(nodo[0])
        inorden(nodo[2], resultado)
    return resultado

def postorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo is None:
        return resultado
    if es_hoja(nodo):
        resultado.append(nodo[0])
    else:
        postorden(nodo[1], resultado)
        postorden(nodo[2], resultado)
        resultado.append(nodo[0])
    return resultado