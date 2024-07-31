from flask import Flask, make_response, jsonify
from model import db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


<<<<<<< HEAD
@app.route('/api/products')
=======
@app.route('/api/v1/products')
>>>>>>> 38619add5693761e3ca995cde765f9a67530344f
def getAllProducts():
    return make_response(jsonify({"products": db}), 200)


if __name__ == '__main__':
    app.run()
