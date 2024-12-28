from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    nickname = data['nickname']
    message = data['message']
    emit('message', {'message': message, 'nickname': nickname}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='192.168.22.6', port=5000)
