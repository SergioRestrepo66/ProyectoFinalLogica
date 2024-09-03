import random


def crearTablero(dimension):
    return [["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrarTableros(tableroDisparosJugador, tableroDisparosOponente):
    print("\n Tablero de Disparos: ")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    print("\n Tablero de disparos del oponente: ")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))

def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
                if jugador == "jugador":
                    print(f"colocado {barco ['nombre']} de tamaño {barco['dimension']}")
                    fila= int(input("Ingrese la fila: "))
                    columna = int(input("Ingrese la columna: "))
                    orientacion = input("Ingrese la orientacion (h para horizontal, v para vertical): ").lower()
                else:
                     fila = random.randint(0, len(tablero)-1)
                     columna = random.randint(0, len(tablero)-1)
                     orientacion = random.choice(['h', 'v'])

                if validadrColocacion(tablero, fila, columna, barco['dimension'], orientacion):
                     colocarBarco(tablero, fila, columna, barco['dimension'], orientacion)
                     colocado = True
                elif jugador == "jugador":
                     print("Colocacion es invalida. Intenta de nuevo")


def validadrColocacion(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila][columna+i] != "~":
                return False
    else:
        if fila + dimension>len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila+i][columna] != "~":
                return True
    return True

def colocarBarco(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero[fila][columna+i]= "B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna]= "B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"
        return "Impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] ="O"
        return "Agua"
    return "Ya disparaste aqui"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True

def jugarContraComputadora():
    dimension = 5
    tableroJugador = crearTablero(dimension)
    tableroComputador = crearTablero(dimension)
    tableroDisparosJugador = crearTablero(dimension)
    tableroDisparosComputadora = crearTablero(dimension)
    barcos = [
        {"nombre":"Portaaviones", "dimension":3},
        {"nombre": "Submarino", "dimension":2}
    ]
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "jugador")
    colocarBarcos(tableroComputador, barcos, "Computador")
    turnoJugador=True
    while True:
        if turnoJugador:
            print("\ntu turno")
            mostrarTableros(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingresa la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resulta = realizarDisparo(tableroDisparosComputadora, tableroDisparosJugador, fila, columna)
            if verificarVictoria(tableroComputador):
                print("Ganaste")
                return "Jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado} ")
            if verificarVictoria(tableroJugador):
                print("La computadora gano ")
                return "Computadora"
        turnoJugador = not turnoJugador

def jugarDosJugadores():
    dimension = 5
    tableroJugador1 = crearTablero(dimension)
    tableroJugador2 = crearTablero(dimension)
    tableroDisparosJugador1 = crearTablero(dimension)
    tableroDisparosjugador2 = crearTablero(dimension)
    barcos = [
        {"nombre":"Portaaviones", "dimension":3},
        {"nombre": "Submarino", "dimension":2}
    ]
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador1, barcos, "jugador")
    print("Jugador 2 Coloca tus barcos")
    colocarBarcos(tableroJugador2, barcos, "jugador")
    turnoJugador1=True
    while True:
        if turnoJugador1:
            print("\nTurno del Jugador 1")
            mostrarTableros(tableroDisparosJugador1, tableroDisparosjugador2)
            fila = int(input("Ingresa la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparosJugador1, fila, columna)
            if verificarVictoria(tableroJugador2):
                print("Jugador 1 gano")
                return "jugador 1"
        else:
            print("\nTurno del jugador 2")
            mostrarTableros(tableroDisparosjugador2, tableroDisparosJugador1)
            fila = int(input("Ingresa la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resultado = realizarDisparo(tableroJugador1, tableroDisparosjugador2, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado} ")
            if verificarVictoria(tableroJugador1):
                print("El jugador 2 gano ")
                return "Jugador 2"
        turnoJugador1 = not turnoJugador1
def mostrarMenu():
    print("¡Bienvenido a Batalla Naval! ")
    print("Selecciona contra quien quieres jugar ")
    print("1. Contra Computadora")
    print("2. Contra Jugador")
    print("3. Salir")

def IniciarJuego():
    while True:
        mostrarMenu()
        modo = input("Elige una opcion: ")
        if modo == "1":
            ganador = jugarContraComputadora()
        elif modo == "2":
            ganador = jugarDosJugadores()
        elif modo == "3":
            print("Gracias por jugar con Pio Pio")
            break
        else:
            print("Opcion no valida, por favor elige la opcion correcta")
            continue
        print(f"El ganador es {ganador}")
        jugarDeNuevo = input("Quieres jugar de nuevo? (s/n) ").lower()
        if jugarDeNuevo !="s":
            print("Gracias por jugar, ¡Esperemos que pronto vuelvas a jugar Batalla Naval!")
            break

IniciarJuego()






        


         
             
     







