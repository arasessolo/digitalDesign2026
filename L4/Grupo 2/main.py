import random
import time
def analizar_densidad():
    numero = random.randint (1,100)
    return numero

def iniciar_escaneo():
    resultado = analizar_densidad()

    if resultado >= 50:
            print("Densidad alta: Iniciando excavación")
    else:
            print("Densidad baja: Buscando otra zona.")

iniciar_escaneo()
        
def perforar():
    profundidad = 0
    while profundidad <= 10:
          profundidad = profundidad + 1
          print ("Perforando.. metros actuales:" + str(profundidad) )
          
    print ("Proceso de perforación finalizado")
perforar ()
        

def verificar_visibilidad():
      cielo = input("Intruducir como esta el cielo (despejado o con tormenta): ")
      return cielo

def navegar_a_base():
      kilometros_recorridos = 0 
      objetivo = 3
      print("Iniciando sistema de navegación automática...")
      while kilometros_recorridos < objetivo:
        respuesta_c = verificar_visibilidad()
        if respuesta_c == "despejado":
             kilometros_recorridos = kilometros_recorridos + 1
             print("Avanzando…")
             time.sleep(1)
        else:
             print("Tormenta detectada, esperando...")
             time.sleep(1)
      print("¡Misión cumplida! El Rover ha llegado a la base a salvo.")
navegar_a_base()
        