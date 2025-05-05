from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

# Home route (health check)
@app.route("/", methods=["GET"])
def home():
    return "Order Service is running!", 200

# Test endpoint with Swagger doc
@app.route("/test", methods=["GET"])
def test():
    """
    A simple test endpoint
    ---
    responses:
      200:
        description: Test successful
    """
    return "Swagger is working!", 200

# Place order route
@app.route("/place-order", methods=["POST"])
def place_order():
    """
    Place a new order
    ---
    parameters:
      - name: user_id
        in: json
        type: string
        required: true
      - name: item_id
        in: json
        type: string
        required: true
    responses:
      200:
        description: Order placed successfully
      400:
        description: Missing required fields
    """
    data = request.get_json()

    if not data or 'user_id' not in data or 'item_id' not in data:
        return jsonify({"error": "Missing user_id or item_id"}), 400

    user_id = data['user_id']
    item_id = data['item_id']

    # Normally you'd call inventory-service and payment-service here
    return jsonify({
        "message": "Order placed successfully",
        "user_id": user_id,
        "item_id": item_id
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
