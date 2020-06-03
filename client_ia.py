# Universidad del Valle de Guatemala
# Inteligencia Artificial - Seccion 10
# Proyecto final - Dots and boxes
# Maria Fernanda Estrada 14198
# 03/06/2020


# Librerias y funciones
import socketio
import random
from minimax_fun import minimax

# Datos conexion al servidor
sio = socketio.Client()
tournamentID = '5000'
username = 'Maria Estrada'

# Conectar al servidor
@sio.event
def connect():
    # Informacion que se envia para establecer conexion o signin
    sio.emit('signin',
        {
            'tournament_id': tournamentID,
            'user_role': 'player',
            'user_name': username
        }
    )
    # Si funciono
    print('Connected to server')

# Realizar jugada 
@sio.event
def ready(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    board = data['board']
    movement = minimax(board, playerTurnID)
    # Emitir datos de jugada
    sio.emit('play',
        {
            'tournament_id': tournamentID,
            'player_turn_id': playerTurnID,
            'game_id': gameID,
            'movement': movement
        }
    )
    
# Al terminar partida, colocar al jugador en ready para nueva partida
@sio.event
def finish(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    # Datos para colocar a player en ready
    sio.emit('player_ready',
        {
            'tournament_id': tournamentID,
            'player_turn_id': playerTurnID,
            'game_id': gameID,
        }
    )

# Desconectar del servidor
@sio.event
def disconnect():
    print('Disconnected from server')

# IPs
sio.connect('http://3.12.129.126:5000')
#sio.connect('http://127.0.0.1:4000')

sio.wait()