from flask import Flask

from chessbattle.utils import static_path

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    with open(static_path('index.html'), 'r') as f:
        return f.read()


def main():
    app.run(debug=True, use_reloader=False)
