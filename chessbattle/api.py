from flask import jsonify, Response

from chessbattle.server import app
from chessbattle.server import game


@app.route('/board/<int:uid>', methods=['GET'])
def board_state(uid):
    return jsonify(game.serialize())


@app.route('/board/<int:uid>/svg', methods=['GET'])
def board_state_svg(uid):
    return Response(game.to_svg(), mimetype='image/svg+xml')
