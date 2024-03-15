from flask import Flask,render_template,request,redirect,url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio =  SocketIO(app)

@app.route('/')
def home():
    return render_template("chat1.html")

@app.route('/chat')
def chat():
    username = request.args.get("username")
    roomid  = request.args.get("roomid")

    if username and roomid:
        return render_template("chat2.html",username = username,roomid =roomid)
    else:
        return redirect(url_for("home"))

@socketio.on("join_room")
def handle_join_room_event(data):
    app.logger,info("{} has joined the room {}".format(data["username"], data["roomid"]))


if __name__ == "__main__":
    socketio.run(app,host ="0.0.0.0",port=5005)

