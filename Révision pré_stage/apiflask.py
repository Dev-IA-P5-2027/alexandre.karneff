from flask import Flask, redirect, url_for, jsonify, abort
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("say_hello"))

@app.route('/hello', methods=['GET'])
def say_hello():
    return "Hello World!"
    # À compléter et documenter

    
@app.route('/time', methods=['GET'])
def give_time():
    now = datetime.datetime.now()
    now_json = jsonify(now)
    return now_json


@app.route('/add', methods=['GET'])
def add_numbers(a=5,b='10'):
    if type(a) in (int,float) and type(b) in (int,float):
        return f"La somme de {a} et {b} est {a+b}"
    else :
        abort(400, description="Les nombres sont invalides pour l'addition")

if __name__ == '__main__':
    app.run(debug=True)
