from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/", methods=["GET"])
def home():
    return "User Service is up and running!", 200

@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user
    ---
    tags:
      - User
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: User registered successfully
      400:
        description: Missing username or password
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    # Simulated user creation logic
    return jsonify({"message": f"User {username} registered successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
