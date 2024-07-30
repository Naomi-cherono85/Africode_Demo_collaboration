from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import routes and register them with the app
with app.app_context():
    db.create_all()

from app import routes


