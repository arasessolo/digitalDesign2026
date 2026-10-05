import time
padron_mascotas = {
    "Luna" : {"especie": "labrador", "edad": 5, "vacunas_cant": 3},
    "Aurora" : {"especie": "golden", "edad": 7, "vacunas_cant": 5},
    "Estrellita" : {"especie": "pomeraña", "edad": 3, "vacunas_cant": 1},
}
lista_adoptante= []
time.sleep(1)


def registrar_mascota(nombre_mascota, especie):
    padron_mascotas[nombre_mascota] = {"especie": especie, "vacunas_cant":0 }
    time.sleep(1)


def aplicar_vacuna(nombre_mascota, vacunas_cant):
    if nombre_mascota in padron_mascotas:
        nombre_mascota["vacunas_cant"] = nombre_mascota["vacunas_cant"] + vacunas_cant
    time.sleep(1)


def ver_padron() :
    if not padron_mascotas:
        print("El padrón del refugio se encuentra actualmente vacío.")
    else: 
        print("--- PADRÓN DE MASCOTAS ---")
        for mascota in padron_mascotas:
            especie = padron_mascotas[mascota]["especie"]
            vacunas = padron_mascotas[mascota]["vacunas_cant"]
            print(f"Mascota: {mascota} + Especie: {especie} + Vacunas aplicadas: {vacunas}")
        time.sleep(1)


def reportar_aptos_adopcion() :
    if not padron_mascotas:
        print("El padrón se encuentra actualmente vacío.")
    else:
        print("--- MASCOTAS APTAS PARA ADOPCIÓN INMEDIATA ---")
        aptos_encontrados = 0
        for mascota in padron_mascotas:
            vacunas = padron_mascotas[mascota]["vacunas_cant"]
    if vacunas >= 3:
        especie = padron_mascotas[mascota]["especie"]
        print(f" Apto: {mascota} + Especie: {especie} + Vacunas: {vacunas}")
        aptos_encontrados += 1
    if aptos_encontrados == 0:
            print("Actualmente no hay mascotas en el refugio con 3 o más vacunas aplicadas.")
    time.sleep(1)


def agregar_a_espera_adopcion(nombre_adoptante):
    if nombre_adoptante in lista_adoptante :
        print("Ya estas registrado")
    else:
        lista_adoptante.append(nombre_adoptante)
        ordennumero= lista_adoptante.index(nombre_adoptante) + 1
        print("Tu numero de orden es" + str(ordennumero))
        print(lista_adoptante)
    time.sleep(1)



def atender_siguiente_adoptante() :
    if not lista_adoptante: 
        print("la lista de espera se encuentra vacía”")
    else:
        adoptante = lista_adoptante[0]
    print("atendiendo a ” + adoptante")
    print("se realizará la entrevista para y la asignación el adoptante")
    lista_adoptante.remove(adoptante)
    time.sleep(1)



def remover_de_espera_adopcion(nombre_adoptante):
    if nombre_adoptante in lista_adoptante:
        lista_adoptante.remove(nombre_adoptante)
        print("el adoptante fue eliminado de la lista de espera")
    time.sleep(1)


def salir() :
    print("Gracias por acompañarnos. ¡Hasta luego!")
    time.sleep(1)


def menu() :
    a = True
    while a: 
        print("     SISTEMA DE GESTIÓN DEL REFUGIO     ")
        print("1. Registrar nueva mascota")
        print("2. Aplicar vacuna a mascota")
        print("3. Ver padrón completo de mascotas")
        print("4. Ver reporte de mascotas aptas para adopción")
        print("5. Agregar adoptante a lista de espera")
        print("6. Atender siguiente adoptante")
        print("7. Remover adoptante de lista de espera")
        print("8. Salir")


        opcion = input("Elige un numero del (1-8)")
        if opcion == "1":
            nombre_mascota = input("Nombre de la mascota: ")
            especie = input("Especie de la mascota: ")
            registrar_mascota(nombre_mascota, especie)

        elif opcion == "2":
            nombre_mascota = input("Nombre de la mascota a vacunar: ")
            vacunas_cant = int(input("Cuantas vacunas tiene la mascota"))
            aplicar_vacuna(nombre_mascota, vacunas_cant)

        elif opcion == "3" :
            ver_padron()

        elif opcion == "4" :
            reportar_aptos_adopcion()

        elif opcion == "5" :
            nombre = input("Nombre del adoptante: ")
            agregar_a_espera_adopcion(nombre)

        elif opcion == "6" :
            atender_siguiente_adoptante()

        elif opcion == "7" :
            nombre = input("Nombre del adoptante a remover: ")
            remover_de_espera_adopcion(nombre)

        elif opcion == "8" :
            salir()
            a = False

        else:
            print("Opción inválida. Por favor, seleccione un número del 1 al 8.")
        a = False

menu()

        
        

  


