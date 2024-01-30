from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

# Home page - Input form
@app.route('/')
def input_form():
    return render_template('input_form.html')

# Display the input
@app.route('/display', methods=['POST'])
def display():
    try:
        user_input = request.form['user_input']
        return render_template('display_result.html', user_input=user_input)

    except Exception as e:
        print(e)
        abort(500)  # Internal Server Error

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5002)

