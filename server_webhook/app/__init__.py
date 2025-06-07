from flask import Flask
from app.extensions import mongo
from flask_cors import CORS
import os

# Creating our flask app
def create_app():

    app = Flask(__name__)

    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo.init_app(app)

    try:
        with app.app_context():
            mongo.cx.server_info() 
            print("MongoDB connection successful. ")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

    CORS(app)

    from app.webhook.routes import webhook

    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
