# order_management (Order Management) - Python code with Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample order data (replace with your actual order data)
orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    orders.append(data)
    return "Order created successfully!", 201

@app.route('/orders')
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003)
