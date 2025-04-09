from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
from auth import auth_blueprint
from chatbot import chatbot_blueprint
from recommendation import recommendation_blueprint
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)
CORS(app)

app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
app.register_blueprint(chatbot_blueprint, url_prefix='/api/chat')
app.register_blueprint(recommendation_blueprint, url_prefix='/api/recommendations')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)