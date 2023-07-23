# microservice1 (Product Catalog) - Python code with Flask
from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data (replace with your actual product data)
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99},
    {"id": 3, "name": "Product 3", "price": 5.99},
]

@app.route('/products')
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
