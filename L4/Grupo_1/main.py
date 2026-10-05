import random
import time

# --- FUNCIONES DE LOS JUEGOS ---

def juego1():
    print("\n=== Bienvenidos al Juego 1: Adivinar el número ===")
    
    # Paso 1: Preparar las variables
    numero_secreto = random.randint(1, 10)
    intentos = 5
    puntos = 50
    adivino = "no"
    
    # Paso 2: El Bucle
    while intentos > 0 and adivino == "no":
        print("\nTe quedan", intentos, "intentos y tenes", puntos, "puntos.")
        numero_usuario = int(input("Ingresa un número del 1 al 10: "))
        
        if numero_usuario == numero_secreto:
            print("¡Ganaste! Adivinaste el número.")
            print("Puntos totales:", puntos)
            adivino = "si"
        else:
            intentos = intentos - 1
            puntos = puntos - 10
            if intentos > 0:
                print("Incorrecto, proba de nuevo.")
                
    # Paso 3: El Final
    if adivino == "no":
        print("\nTe quedaste sin intentos. El número era...", numero_secreto)


def juego2():
    print("\n=== Bienvenidos al Juego 2: La Batalla ===")
    
    # Paso 1: Variables iniciales
    vida_jugador = 100
    vida_cpu = 100
    
    # Paso 2: Bucle de la batalla
    while vida_jugador > 0 and vida_cpu > 0:
        print("\n--------------------------------")
        print("Tu vida:", vida_jugador)
        print("Vida de la CPU:", vida_cpu)
        print("--------------------------------")
        
        # Turno del Jugador
        print("¿Que queres hacer?")
        print("1 - Atacar")
        print("2 - Curar")
        opcion_jugador = int(input("Elegi una opcion (1 o 2): "))
        
        if opcion_jugador == 1:
            danio = random.randint(10, 50)
            vida_cpu = vida_cpu - danio
            print("Atacaste a la CPU y le quitaste", danio, "de vida!")
        elif opcion_jugador == 2:
            curacion = random.randint(1, 20)
            vida_jugador = vida_jugador + curacion
            print("Te curaste", curacion, "puntos de vida!")
        else:
            print("Opcion invalida, perdiste el turno.")
            
        time.sleep(1)
        
        # Turno de la CPU (si sigue viva)
        if vida_cpu > 0:
            accion_cpu = random.randint(1, 2)
            if accion_cpu == 1:
                danio_cpu = random.randint(10, 50)
                vida_jugador = vida_jugador - danio_cpu
                print("La CPU te ataco y te quito", danio_cpu, "de vida!")
            else:
                curacion_cpu = random.randint(1, 20)
                vida_cpu = vida_cpu + curacion_cpu
                print("La CPU se curo", curacion_cpu, "puntos de vida!")
                
        time.sleep(1)

    # Paso 3: Quien gano
    print("\n=========================")
    if vida_jugador > 0:
        print("¡Victoria! Derrotaste a la CPU")
    else:
        print("Game Over. La CPU ha ganado")
    print("=========================")


# --- ESTRUCTURA PRINCIPAL DEL SISTEMA ---

def comenzarJuego():
    print("-- Bienvenido a Arcade Python --")
    continuar = "si"
    
    while continuar == "si":
        print("\nTenemos estos juegos disponibles:")
        print("1 - Juego 1: Adivinar el número")
        print("2 - Juego 2: La Batalla")
        print("3 - Salir del Arcade")
        
        opcion_input = input("\nIngresa el numero de opcion: ")
        
        if opcion_input.isdigit():
            opcion = int(opcion_input)
            
            if opcion == 1:
                juego1()
            elif opcion == 2:
                juego2()
            elif opcion == 3:
                continuar = "no"
                break
            else:
                print("Error: Opción no válida")
        else:
            print("Error: Opción no válida")
            
        # Si no se eligió salir directamente, pregunta si quiere elegir otro
        if continuar != "no":
            respuesta = input("\n¿Querés elegir otro juego? (si/no): ").lower()
            if respuesta != "si":
                continuar = "no"

    print("\nGracias por jugar en Arcade Python. ¡Te esperamos pronto!")


# Ejecutamos la funcion principal para arrancar
comenzarJuego()