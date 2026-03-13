from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connexion et création de la table SQLite3
def init_db():
    with sqlite3.connect("books.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            year INTEGER NOT NULL)''')
        conn.commit()

# Insérer des données par défaut
def insert_default_books():
    with sqlite3.connect("books.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]

        if count == 0:
            books = [
                ("Le Petit Prince", "Antoine de Saint-Exupéry", 1943),
                ("1984", "George Orwell", 1949),
                ("L'Alchimiste", "Paulo Coelho", 1988),
                ("Les Misérables", "Victor Hugo", 1862),
                ("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997)
            ]
            cursor.executemany(
                "INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books
            )
            conn.commit()

# Initialiser la base de données
init_db()
insert_default_books()

# Endpoint pour récupérer tous les livres
@app.route('/books', methods=['GET'])
def get_books():
    with sqlite3.connect("books.db") as conn:
        cursor = conn.cursor()
        books = cursor.execute("SELECT * FROM books").fetchall()
        return books
        
    
if __name__ == '__main__':
    app.run(debug=True)