from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=False,host='0.0.0.0')
