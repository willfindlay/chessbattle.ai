from flask import Flask, send_from_directory

from chessbattle.defs import STATIC_PATH

# TODO: get rid of this import when we no longer need it
from chessbattle.game import Game

# FIXME: we just have one game for now, in the future we want a database
# of games
game = Game()

# Initialize the app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory(STATIC_PATH, 'index.html')


# Import API routes here
import chessbattle.api


@app.route('/<path:path>')
def path(path):
    return send_from_directory(STATIC_PATH, path)


def main(args=None):

    # Run the server
    app.run(debug=True, use_reloader=False)
