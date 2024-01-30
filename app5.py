from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session security (replace with your actual secret key)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        user_data = session.get('user_data', {})
        return render_template('welcome.html', username=username, user_data=user_data)
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Here you can fetch user-specific data from a database or any other source
        user_data = {'email': 'user@example.com', 'age': 25}  # Example user data
        session['username'] = username
        session['user_data'] = user_data
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_data', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5001)
