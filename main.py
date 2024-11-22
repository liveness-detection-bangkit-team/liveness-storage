from flask import Flask
from flask_cors import CORS
from src.routes import routes
from src.rateLimiter import create_db

# Initialize Flask app and Limiter
app = Flask(__name__)
# limiter = Limiter(app=app, key_func=get_remote_address, default_limits=["30 per minute"])

# Register the routes blueprint to the Flask app
app.register_blueprint(routes)

# Enable CORS for all endpoints
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["*"],
            "methods": ["GET", "POST", "DELETE", "PUT"],
        },
    },
    supports_credentials=True,
)

# Create the rate limit database
create_db()

# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)