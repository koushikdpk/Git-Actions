# frontend (Frontend) - Python code with Flask and requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Backend service URLs (replace with actual URLs)
product_catalog_url = "http://product_catalog:8001/products"
user_management_url = "http://user_management:8002/users/"
order_management_url = "http://order_management:8003/orders"

@app.route('/')
def index():
    products = requests.get(product_catalog_url).json()
    return render_template('index.html', products=products)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        payload = {"username": username, "email": email}
        response = requests.post(user_management_url, json=payload)
        return response.text
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        response = requests.get(user_management_url + username)
        user_info = response.json()
        return f"Welcome, {user_info['username']}! Your email is {user_info['email']}."
    return render_template('login.html')

@app.route('/create_order', methods=['POST'])
def create_order():
    user_id = 1  # Replace with actual user ID from login information
    payload = {"user_id": user_id, "order_items": ["item1", "item2", "item3"]}
    response = requests.post(order_management_url, json=payload)
    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8004)
