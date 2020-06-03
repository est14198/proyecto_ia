# Universidad del Valle de Guatemala
# Inteligencia Artificial - Seccion 10
# Proyecto final - Dots and boxes
# Maria Fernanda Estrada 14198
# 03/06/2020


# Librerias
from copy import copy, deepcopy


# Funcion minimax con 3-lookahead y alpha-beta
def minimax(tablero):
    copya = deepcopy(tablero)
    valor_minimax = 0
    movimiento = [-1,-1]

    for i in range(60):
        valor_minimax_i = 0
        copya2 = deepcopy(copya)
        max_i = False

        if copya2[0 if i < 30 else 1][i%30] == 99:
            resultado = puntos_movimiento(copya2, [0 if i < 30 else 1, i%30], True)
            
            if resultado > 0:
                max_i = True
            
            for j in range(60):
                valor_minimax_j = 0
                max_j = False
                
                if copya2[0 if j < 30 else 1][j%30] == 99:
                    resultado = puntos_movimiento(copya2, [0 if j < 30 else 1, j%30], max_i)
                    
                    if resultado > 0 and max_i:
                        max_j = True
                    elif resultado == 0 and max_i == False:
                        max_j = True
                    
                    for k in range(60):  
                        if copya2[0 if k < 30 else 1][k%30] == 99:
                            resultado = puntos_movimiento(copya2, [0 if k < 30 else 1, k%30], max_j)
                            
                            if max_j and resultado >= valor_minimax_j:
                                valor_minimax_j = resultado
                            elif max_j == False and resultado <= valor_minimax_j:
                                valor_minimax_j = resultado

                            if max_i and max_j == False:
                                if valor_minimax_i >= valor_minimax_j:
                                    break
                            
                            if max_j and max_i == False:
                                if valor_minimax_j >= valor_minimax_i:
                                    break
                    
                    if max_i and valor_minimax_j >= valor_minimax_i:
                        valor_minimax_i = valor_minimax_j
                    elif max_i == False and valor_minimax_j <= valor_minimax_i:
                        valor_minimax_i = valor_minimax_j

                    if max_i == False:
                        if valor_minimax >= valor_minimax_i:
                            break

            if valor_minimax_i >= valor_minimax:
                valor_minimax = valor_minimax_i
                movimiento = [0 if i < 30 else 1, i%30]

    return movimiento


# Calcular puntos por movimiento
def puntos_movimiento(tablero, movimiento, player):
    puntos_antes = 0
    puntos_despues = 0
    acumulador = 0
    contador = 0

    for i in range(30):
        if(((i + 1) % 6) != 0):
            if(tablero[0][i] != 99 and tablero[0][i + 1] != 99 and tablero[1][contador + acumulador] != 99 and tablero[1][contador + acumulador + 1] != 99):
                puntos_antes += 1
            acumulador += 6
        else:
            contador += 1
            acumulador = 0

    tablero[movimiento[0]][movimiento[1]] = 0

    acumulador = 0
    contador = 0

    for i in range(30):
        if(((i + 1) % 6) != 0):
            if(tablero[0][i] != 99 and tablero[0][i + 1] != 99 and tablero[1][contador + acumulador] != 99 and tablero[1][contador + acumulador + 1] != 99):
                puntos_despues += 1
            acumulador += 6
        else:
            contador += 1
            acumulador = 0
    
    puntos = puntos_despues - puntos_antes

    if player:
        tablero[movimiento[0]][movimiento[1]] = puntos
    else:
        tablero[movimiento[0]][movimiento[1]] = -puntos

    return puntos


# Heuristica: determinar a cuantos cuadros les falta una rallita para cerrar.
def heuristica(tablero, player):
    print("noooo")



"""cuadros = [
    [[0,1][0,1]],
    [[6,7][1,2]],
    [[12,13][2,3]],
    [[18,19][3,4]],
    [[24,25][4,5]],
    [[1,2][6,7]],
    [[7,8][7,8]],
    [[13,14][8,9]],
    [[19,20][9,10]],
    [[25,26][10,11]],
    [[2,3][12,13]],
    [[8,9][13,14]],
    [[14,15][14,15]],
    [[20,21][15,16]],
    [[26,27][16,17]],
    [[3,4][18,19]],
    [[9,10][19,20]],
    [[15,16][20,21]],
    [[21,22][21,22]],
    [[27,28][22,23]],
    [[4,5][24,25]],
    [[10,11][25,26]],
    [[16,17][26,27]],
    [[22,23][27,28]],
    [[28,29][28,29]]
]"""