import sys
from operator import itemgetter

MAX = 1
MIN = -1
_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

global jugada_maquina

def minimax(tablero, jugador):
    global jugada_maquina
    if game_over(tablero):
        return [ganador(tablero), 0]
    
    movimientos = []
    for jugada in range(0, len(tablero)):
        if tablero[jugada] == 0:
            tableroaux = tablero[:]
            tableroaux[jugada] = jugador
            puntuacion = minimax(tableroaux, jugador * (-1))
            movimientos.append([puntuacion, jugada])
    
    if jugador == MAX:
        movimiento = max(movimientos, key=str)        
        jugada_maquina = movimiento[1]
        return movimiento 
    else:       
        movimiento = min(movimientos, key=str)        
        return movimiento[0]

def game_over(tablero):
    no_tablas = False
    for i in range(0, len(tablero)):
        if tablero[i] == 0:
            no_tablas = True
            
    if ganador(tablero) == 0 and no_tablas:
        return False
    else:
        return True

def ganador(tablero):
    lineas = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5,8], [0, 4, 8], [2, 4, 6]]
    ganador = 0
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] and tablero[linea[0]] == tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador = tablero[linea[0]]
    return ganador

def ver_tablero(tablero):
    board = list(map(str, tablero))    
    for i in range(0, len(tablero)):
        if tablero[i] == MAX:
            board[i] = _PLAYER_SYMBOL
        elif tablero[i] == MIN:
            board[i] = _MACHINE_SYMBOL
        else:
            board[i] = ' '
  
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')    

def player_turn(tablero):
    ok= False
    while not ok:
        casilla = input("¿Cual casilla vas a escoger?")
        if str(casilla) in '0123456789' and len(str(casilla)) == 1 and tablero[int(casilla)-1] == 0:
            tablero[int(casilla)-1] = MIN
            ok = True
        if casilla == "exit":
            sys.exit(0)
    return tablero

def machine_turn(tablero):
    global jugada_maquina
    punt = minimax(tablero[:], MAX)
    tablero[jugada_maquina] = MAX
    return tablero

if __name__ == "__main__":
    print("Ponga el numero de la casilla donde desea iniciar o escriba exit para salir")
    tablero = [0,0,0,0,0,0,0,0,0]
    
    while(True):
        ver_tablero(tablero)
        tablero = player_turn(tablero)
        if game_over(tablero):
            break
        
        tablero = machine_turn(tablero)
        if game_over(tablero):
            break
            
    ver_tablero(tablero)
    g = ganador(tablero)
    if g == 0:
        gana = "Tablas"
    elif g == MIN:
        gana = "Jugador"
    else:
        gana = "Ordenador"
    
    if gana=="Tablas":
      print("No hay ganador. El juego quedo en tablas")
    else:
      print("Ganador: " + gana)
      