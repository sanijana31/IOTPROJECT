from flask_cors import CORS
from flask import Flask, jsonify, request
from random import randrange, uniform
import Mqtt_Publisher_Clint as M
import Proximity_sensor as sensor

Mqtt_obj=M.MQTT("proximity")
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
    max_volt,min_volt = int(books_db[1]["vmax"]), int(books_db[1]["vmin"])
    max_dis,min_dis = int(books_db[1]["imax"]), int(books_db[1]["imin"])
    proximity_sensor=sensor.Proximity(max_volt,min_volt,max_dis,min_dis)
    data=proximity_sensor.proximity_output()
    Mqtt_obj.Publish_Data_To_Server(data)
    return jsonify(data)
@app.route('/stop', methods=['POST'])
def stop():
    stop=request.get_json()
    msg="MQTT stop"
    return jsonify(msg)










app.run(port=5000)