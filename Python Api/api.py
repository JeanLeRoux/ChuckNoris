from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)



@app.route('/categories', methods=['GET'])
def categories():
    """
    --------------------
    | Insert Code Here |
    --------------------
    """
    return make_response(jsonify("return_value"), 200)
    
@app.route('/jokeFromCategory', methods=['GET'])
def jokeFromCategory():
    category = request.args.get('category')
    
    """
    --------------------
    | Insert Code Here |
    --------------------
    """

    return make_response(jsonify(category), 200)

@app.route('/random', methods=['GET'])
def random():
    """
    --------------------
    | Insert Code Here |
    --------------------
    """
    return make_response(jsonify("return_value"), 200)
    
if __name__ == '__main__':
    app.run(host='192.168.0.105', port=3000, debug=True)