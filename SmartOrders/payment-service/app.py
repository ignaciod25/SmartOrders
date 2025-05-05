from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def process_payment():
    if random.random() < 0.3:
        return jsonify({"error": "Simulated payment failure"}), 500
    return jsonify({"status": "Payment processed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)