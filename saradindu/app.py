from flask_cors import CORS
from flask import Flask, jsonify, request
from random import randrange, uniform

app = Flask(__name__)
CORS(app)

books_db = [
    {
       
        
    }
  
]


# retrieve all the books   http://127.0.0.1:5000/books
@app.route('/books')
def get_all_book():
    return jsonify({'books':books_db})

# retrieve one book  http://127.0.0.1:5000/book/Secret
@app.route('/book/<string:name>')
def get_book(name):
    for book in books_db:
        if book['name'] == name:
            return jsonify(book)
    
    return jsonify({'message':'book not found'})



# create a book  http://127.0.0.1:5000/book/
@app.route('/book', methods=['POST'])
def create_book():
    body_data = request.get_json()
    books_db.append(body_data)
    total = int(books_db[1]["vmax"]) + int(books_db[1]["vmin"])
    total=total*uniform(2.0, 10.0)
    return jsonify(total)









app.run(port=5000)