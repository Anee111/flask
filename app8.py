from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session security (replace with your actual secret key)

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Dummy user data (replace with your actual user data and authentication logic)
class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

# Replace this list with a database query in a real application
users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2'),
    # ... add more users as needed
]

@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((user for user in users if user.username == username and user.password == password), None)

        if user:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login1.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Dummy user ID (replace with database logic to generate unique user IDs)
        user_id = len(users) + 1

        new_user = User(user_id, username, password)
        users.append(new_user)

        login_user(new_user)
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port =5002)

