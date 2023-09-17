from flask import Flask, request, jsonify
import pyodbc as odbc


app = Flask(__name__)

def db_connect():
    conn= None
    try:      
        conn = odbc.connect('Driver={SQL Server};'
                            'Server=34.163.246.196;'
                            'Database=LIBRARY;'
                            'UID=sqlserver;'
                            'PWD=admin;'
                            )
    except odbc.Error as e:
        print(e)

    return conn

@app.route('/books', methods=["GET", "POST"])
def books():
    conn= db_connect()
    cursor= conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM BOOKS")
        books= [dict(id=row[0], author=row[1], title=row[2]) for row in cursor.fetchall()]
        if books is not None: 
            return jsonify(books)

    if request.method == "POST":
        new_author = request.form["author"]
        new_title = request.form["title"]

        sql = """
            INSERT INTO BOOKS (author, title) VALUES (?,?)
        """
        cursor = cursor.execute(sql, (new_author, new_title))
        conn.commit()
        return f"Book created successfully", 201
    
    
@app.route('/books/<int:id>', methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn= db_connect()
    cursor= conn.cursor()
    book= None

    if request.method == "GET":
        cursor.execute("SELECT * FROM BOOKS WHERE id=?", (id))
        row= cursor.fetchall()
        for r in row:
            book = tuple(r)

        if book is not None:
            return jsonify(book), 200
        else:
            return f"Book with id {id} does not exist", 404
        

    if request.method == "PUT":
        sql= """UPDATE BOOKS 
        SET author=?, title=?
        WHERE id= ?
        """
        new_author = request.form["author"]
        new_title = request.form["title"]
        updated_book= {
            "id": id,
            "author": new_author,
            "title": new_title
        }
        conn.execute(sql, (new_author, new_title, id))
        conn.commit()
        return jsonify(updated_book)
    
    if request.method == "DELETE":
        sql = """DELETE FROM BOOKS WHERE id=?"""
        conn.execute(sql, (id))
        conn.commit()
        return f"Book with id {id} has been successfully deleted", 200

if __name__ == "__main__":
    app.run(debug=True)