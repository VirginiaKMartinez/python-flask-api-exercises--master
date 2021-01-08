from flask import Flask, jsonify, request
import json


app = Flask(__name__)

todos = [ 
    {'label':'My first task', 'done':False},
    {'label':'My second task', 'done':False},
]

@app.route('/todos', methods=['GET'])
def hello_world():
    
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data #recibo data
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request_body) #Convierto la data en diccionario
    print(decoded_object)
    todos.append(decoded_object) #para guardar esa nueva tarea a la lista de todos
    return jsonify(todos), 200 # devolvemos la lista de todos convertida a json gracias al jsonify

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    request_body = request.data
    print("This is the position to delete: ",position)
    decoded_object = json.loads(request_body)
    todos.remove(decoded_object)
    return jsonify(todos), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

