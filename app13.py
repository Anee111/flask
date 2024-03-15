# 13. Implement notifications in a Flask app using websockets to notify users of updates.

# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Example data
data = {'value': 0}

@app.route('/')
def index():
    return render_template('app13index.html', data=data)

@socketio.on('update')
def update_value(new_value):
    data['value'] = new_value
    emit('value_updated', new_value, broadcast=True)
    emit('notification', 'Data has been updated!', broadcast=True)

if __name__ == '__main__':
    socketio.run(app)


