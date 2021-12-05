#import eventlet
#eventlet.monkey_patch() #monkey patch required if i ever need to use eventlet

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
#socketio = SocketIO(app)
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route('/')
def conn_index():
    return render_template('index.html') 

@app.route('/chat')
def conn_chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    send(data, broadcast=True) #broadcast decides who recives the msg

#@socketio.on('disconnect')
#def test_disconnect():
#print('Your buddy has disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
