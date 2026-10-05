import time

# ==========================================
# 1. ESTRUCTURAS DE DATOS CENTRALES
# ==========================================

# Diccionario central para registrar la biblioteca de canciones.
# Clave: titulo de la canción (str)
# Valor: diccionario con 'artista' (str) y 'reproducciones' (int)
biblioteca_canciones = {
    "Viva la Vida": {"artista": "Coldplay", "reproducciones": 1500},
    "Shape of You": {"artista": "Ed Sheeran", "reproducciones": 2300},
    "Bohemian Rhapsody": {"artista": "Queen", "reproducciones": 850}
}

# Lista independiente para la cola de reproducción
cola_reproduccion = []


# ==========================================
# 2. FUNCIONES DEL SOFTWARE
# ==========================================

def agregar_cancion(titulo, artista):
    """
    Da de alta una nueva canción en la biblioteca con 0 reproducciones iniciales.
    Valida que no exista previamente.
    """
    if titulo in biblioteca_canciones:
        print("\n❌ Error: La canción '" + titulo + "' ya existe en la biblioteca.")
    else:
        biblioteca_canciones[titulo] = {
            "artista": artista,
            "reproducciones": 0
        }
        print("\n✅ Canción '" + titulo + "' de '" + artista + "' registrada con éxito.")
    time.sleep(1)


def registrar_reproduccion(titulo, cantidad):
    """
    Suma e incrementa la cantidad de reproducciones de una canción existente.
    """
    if titulo in biblioteca_canciones:
        biblioteca_canciones[titulo]["reproducciones"] = biblioteca_canciones[titulo]["reproducciones"] + cantidad
        total = biblioteca_canciones[titulo]["reproducciones"]
        print("\n✅ Se sumaron " + str(cantidad) + " reproducciones a '" + titulo + "'. Total acumulado: " + str(total) + ".")
    else:
        print("\n❌ Error: La canción '" + titulo + "' no se encuentra en la biblioteca.")
    time.sleep(1)


def ver_biblioteca():
    """
    Muestra todas las canciones de la base de datos con su artista y reproducciones.
    """
    if len(biblioteca_canciones) == 0:
        print("\n⚠️ La biblioteca de canciones se encuentra vacía.")
    else:
        print("\n--- 🎵 BIBLIOTECA DE CANCIONES DE SPOTICLONE ---")
        for titulo in biblioteca_canciones:
            artista = biblioteca_canciones[titulo]["artista"]
            reproducciones = biblioteca_canciones[titulo]["reproducciones"]
            print("• " + titulo + " | Artista: " + artista + " | Reproducciones: " + str(reproducciones))
        print("------------------------------------------------")
    time.sleep(1)


def reportar_hits():
    """
    Filtra y muestra únicamente las canciones que superen las 1000 reproducciones.
    """
    print("\n--- 🔥 REPORTES DE HITS (> 1000 REPRODUCCIONES) ---")
    hay_hits = False
    
    for titulo in biblioteca_canciones:
        if biblioteca_canciones[titulo]["reproducciones"] > 1000:
            reps = biblioteca_canciones[titulo]["reproducciones"]
            artista = biblioteca_canciones[titulo]["artista"]
            print("⭐ " + titulo + " - " + artista + " (" + str(reps) + " reproducciones)")
            hay_hits = True
            
    if not hay_hits:
        print("Actualmente ninguna canción supera las 1000 reproducciones.")
    print("---------------------------------------------------")
    time.sleep(1)


def agregar_a_cola(titulo):
    """
    Agrega una canción existente en la biblioteca al final de la cola de reproducción.
    """
    if titulo not in biblioteca_canciones:
        print("\n❌ Error: La canción '" + titulo + "' debe estar en la biblioteca para ser agregada a la cola.")
    else:
        cola_reproduccion.append(titulo)
        posicion = len(cola_reproduccion)
        print("\n✅ Canción '" + titulo + "' agregada a la cola de reproducción. Posición: N° " + str(posicion) + ".")
    time.sleep(1)


def reproducir_siguiente():
    """
    Remueve y simula la reproducción de la primera canción en la cola.
    """
    if len(cola_reproduccion) == 0:
        print("\n⚠️ La cola de reproducción está vacía.")
    else:
        siguiente = cola_reproduccion.pop(0)
        print("\n▶️ Sonando ahora: '" + siguiente + "'. ¡Disfrutá de la música!")
    time.sleep(1)


def remover_de_cola(titulo):
    """
    Elimina de forma inmediata una canción específica de la cola de reproducción.
    """
    if len(cola_reproduccion) == 0:
        print("\n⚠️ La cola de reproducción se encuentra vacía.")
    elif titulo in cola_reproduccion:
        cola_reproduccion.remove(titulo)
        print("\n🗑️ La canción '" + titulo + "' fue removida de la cola de reproducción.")
    else:
        print("\n❌ Error: La canción '" + titulo + "' no se encuentra en la cola de reproducción.")
    time.sleep(1)


def salir():
    """
    Muestra un mensaje de despedida, realiza una pausa y finaliza la ejecución.
    """
    print("\n👋 Cerrando SpotiClone. ¡Gracias por usar la plataforma de música!")
    time.sleep(1)


# ==========================================
# 3. MENÚ DE CONTROL INTERACTIVO
# ==========================================

def ejecutar_menu():
    """
    Bucle principal del menú interactivo en consola.
    """
    while True:
        print("\n=============================================")
        print("       🎵 SPOTICLONE: EL ALGORITMO          ")
        print("=============================================")
        print("1. Agregar nueva canción")
        print("2. Registrar reproducciones de una canción")
        print("3. Ver biblioteca de canciones")
        print("4. Reportar hits (> 1000 reproducciones)")
        print("5. Agregar canción a la cola de reproducción")
        print("6. Reproducir siguiente canción")
        print("7. Remover canción de la cola")
        print("8. Salir del programa")
        print("=============================================")
        
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            titulo = input("Ingrese el título de la canción: ")
            artista = input("Ingrese el nombre del artista: ")
            agregar_cancion(titulo, artista)

        elif opcion == "2":
            titulo = input("Ingrese el título de la canción: ")
            try:
                cantidad = int(input("Ingrese la cantidad de reproducciones a sumar: "))
                registrar_reproduccion(titulo, cantidad)
            except ValueError:
                print("\n❌ Error: La cantidad de reproducciones debe ser un número entero.")
                time.sleep(1)

        elif opcion == "3":
            ver_biblioteca()

        elif opcion == "4":
            reportar_hits()

        elif opcion == "5":
            titulo = input("Ingrese el título de la canción a agregar a la cola: ")
            agregar_a_cola(titulo)

        elif opcion == "6":
            reproducir_siguiente()

        elif opcion == "7":
            titulo = input("Ingrese el título de la canción a remover de la cola: ")
            remover_de_cola(titulo)

        elif opcion == "8":
            salir()
            break

        else:
            print("\n❌ Opción no válida. Por favor, ingrese un número del 1 al 8.")
            time.sleep(1)


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_menu()