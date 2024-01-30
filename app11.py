from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Home page
@app.route('/')
def index():
    return render_template('index2.html')

# WebSocket event handler for data updates
@socketio.on('update_data')
def handle_update(data):
    # Broadcast the updated data to all connected clients
    socketio.emit('data_updated', data)

if __name__ == '__main__':
    app.run(host ="0.0.0.0",port =5002)

