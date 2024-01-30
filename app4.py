from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template('form.html')

@app.route("/detail", methods=['POST',"GET"])
def check_detail():
    name = request.form.get('name')
    occupation = request.form.get('occupation')
    print(f"Name: {name}, occupation: {occupation}")
    return "Name and occupation received"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
