from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def get_server():
    return "Hello World"


@app.get("/temperature")
def get_temperature():
    temperature = [
        [23.45, 24.12, 23.89, 23.75, 24.01, 24.34],
        [23.81, 23.96, 24.27, 23.55, 23.92, 24.18],
        [24.03, 23.68, 23.94, 23.81, 23.67, 23.92],
    ]
    return jsonify(temperature)


if __name__ == "__main__":
    app.run(debug=True)
