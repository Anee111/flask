from flask import Flask, render_template

app = Flask(__name__)

@app.route('/college')
def college():
    return render_template('college.html')

@app.route('/school')
def school():
    return render_template('school.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000)
