# user_management (User Management) - Python code with Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user data (replace with your actual user data)
users = []

@app.route('/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    users.append(data)
    return "User created successfully!", 201

@app.route('/users/<username>')
def get_user(username):
    user = next((user for user in users if user["username"] == username), None)
    if user:
        return jsonify(user)
    return "User not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)
