from flask import Flask, send_from_directory

from chessbattle.defs import STATIC_PATH

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory(STATIC_PATH, 'index.html')


@app.route('/<path:path>')
def path(path):
    return send_from_directory(STATIC_PATH, path)


#
#
# @app.route('/css/<path:path>', methods=['GET'])
# def css(path):
#    return send_from_directory(static_path('css'), path)
#
#
# @app.route('/js/<path:path>', methods=['GET'])
# def js(path):
#    return send_from_directory(static_path('js'), path)


def main():
    app.run(debug=True, use_reloader=False)
