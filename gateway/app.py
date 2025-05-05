from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/place-order', methods=['POST'])
def place_order():
    data = request.json
    r = requests.post("http://order-service:5002/order", json=data)
    return jsonify(r.json()), r.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)