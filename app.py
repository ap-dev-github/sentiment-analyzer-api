from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello, World!")

@app.route("/hello/<name>")
def hello_name(name):
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(debug=True)