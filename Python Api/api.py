from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import sqlite3
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/addTodo', methods=['POST'])
def add_todo():
      body = request.get_json()
      return make_response(jsonify("return_value"), 200)

@app.route('/deleteTodo', methods=['DELETE'])
def delete_todo():
      """
      --------------------
      | Insert Code Here |
      --------------------
      """
      id = request.args.get("id")
      
      return make_response(jsonify("return_value"), 200)

@app.route('/getTodos', methods=['GET'])
def get_todo():
      return_data = []
      """
      --------------------
      | Insert Code Here |
      --------------------
      """
      return make_response(jsonify(return_data), 200)


@app.route('/randomJoke', methods=['GET'])
def random_joke():
      """
      --------------------
      | Insert Code Here |
      --------------------
      """
      return make_response(jsonify("return_value"), 200)
    
if __name__ == '__main__':
      app.run(host='<change value to your wifi ipv4 address>', port=3000, debug=True)