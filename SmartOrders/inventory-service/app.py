from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/inventory/<item_id>', methods=['GET'])
def check_inventory(item_id):
    # Simulate inventory check
    if item_id == "item1":
        return jsonify({"item_id": item_id, "stock": 5})
    else:
        return jsonify({"item_id": item_id, "stock": 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
