from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/hello',methods=['GET'])
def printHello():
    return "Hello World...!"


@app.route('/add',methods=['GET'])
def getAdd():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return f"Addition of {num1} and {num2} is {num1 + num2}"


@app.route('/sub',methods=['GET'])
def getSub():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return f"{num1} - {num2} is equals {num1 - num2}"


@app.route('/mul',methods=['GET'])
def getMul():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return f"Multiplication of {num1} and {num2} is {num1 * num2}"


@app.route('/div',methods=['GET'])
def getDiv():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return f"{num1} / {num2} is equals {num1 / num2}"


@app.route('/sqr',methods=['GET'])
def getSqr():
    num1 = int(request.args.get('num1'))
    return f"Square of {num1} is {num1*num1}"


@app.route('/')
def home():
   return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)