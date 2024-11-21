from flask import Flask
from snap import snapstory
from ran import ran

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/snapchat/<username>')
def snapchat(username):
    return snapstory(username)


@app.route('/ran')
def ttt():
    return ran()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
