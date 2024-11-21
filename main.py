from flask import Flask
from flask_cors import CORS
from src.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

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

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000, debug=True)