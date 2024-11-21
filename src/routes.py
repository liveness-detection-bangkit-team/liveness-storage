from flask import Blueprint, jsonify, request

# Create a Blueprint for the routes
routes = Blueprint('routes', __name__)

# Define a simple route
@routes.route('/')
def home():
    return "Welcome to the Home Page!"

# Define a dynamic route
@routes.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# Define an API route
@routes.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        data = request.json  # Get JSON data
        return jsonify({"message": "Data received", "data": data}), 201
    else:
        return jsonify({"message": "This is a GET request."}), 200

# Define a 404 error handler
@routes.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404
