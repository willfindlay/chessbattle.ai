from flask import jsonify, Response

from chessbattle.server import app
from chessbattle.server import game

import sqlite3
import pathlib
import os 

def db_connect():
    DEFAULT_PATH =  (str(pathlib.Path().absolute()) + '\chessbattle\db\chessgames.db')#.replace('\\','\\\\')
    print(DEFAULT_PATH)
    con = sqlite3.connect(DEFAULT_PATH)
    return con
    
    
@app.route('/board/<int:uid>', methods=['GET'])
def board_state(uid):
    #print(game.serialize()["board_fen"])
    
    con=db_connect()
    con.set_trace_callback(print)
    cur = con.cursor()
    gameboard_SQL = "INSERT INTO Games (ID, GameInfo) VALUES (?, ?)"
    cur.execute(gameboard_SQL, (uid, game.serialize()["board_fen"]))
    con.commit()
    return jsonify(game.serialize())

@app.route('/board/<int:uid>/svg', methods=['GET'])
def board_state_svg(uid):
    return Response(game.to_svg(), mimetype='image/svg+xml')
