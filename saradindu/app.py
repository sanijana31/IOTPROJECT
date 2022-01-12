from flask_cors import CORS
from flask import Flask, jsonify, request
from random import randrange, uniform
import Mqtt_Publisher_Clint as M
import ldr_sensor as sensor

Mqtt_obj=M.MQTT("Ldr")
Mqtt_obj.Connect_MQTT_Server()

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
    max_res,min_res = int(books_db[1]["vmax"]), int(books_db[1]["vmin"])
    ldr_sensor=sensor.ldr(max_res,min_res)
    data=ldr_sensor.value_gen()
    Mqtt_obj.Publish_Data_To_Server(data)
    return jsonify(data)
@app.route('/stop', methods=['POST'])
def stop():
    stop=request.get_json()
    msg="MQTT stop"
    return jsonify(msg)










app.run(port=5000)