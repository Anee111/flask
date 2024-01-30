from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# Home page - List all books
@app.route('/')
def index():
    return render_template('list_books.html', books=books)

# Add a new book
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add_books.html')

# Edit an existing book
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return redirect(url_for('index'))

    if request.method == 'POST':
        data = request.form
        book["title"] = data["title"]
        book["author"] = data["author"]
        return redirect(url_for('index'))
    return render_template('edit_books.html', book=book)

# Delete a book
@app.route('/delete/<int:book_id>')
def delete(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5002)
