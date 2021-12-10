#import eventlet
#eventlet.monkey_patch() #monkey patch required if i ever need to use eventlet

from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send, emit
#from register import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
#socketio = SocketIO(app)
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route('/')
def conn_index():
    return render_template('index.html')

@app.route('/register')
def register():
    #form = RegistrationForm()
    return render_template('register.html')


@app.route('/test/')
def tester():
    return render_template('nav.html')

@app.route('/chat')
def conn_chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    send(data, broadcast=True) #broadcast decides who recives the msg

if __name__ == '__main__':
    socketio.run(app, debug=True)
