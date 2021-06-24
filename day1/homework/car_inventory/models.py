from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    email = db.Column(db.String(150), nullable = False)
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default="")
    last_name = db.Column(db.String(150), nullable = True, default="")
    password = db.Column(db.String, nullable = True, default="")
    token = db.Column(db.String, default="", unique = True)
    g_auth_verify = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, id="", first_name="", last_name="", password="", token="", g_auth_verify=False):
        self.email = email
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f"User: {self.email} has been added to the database"

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    doors = db.Column(db.String(20))
    seats = db.Column(db.String(20))
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    series = db.Column(db.String(20), nullable=True )
    year = db.Column(db.String(20))
    color = db.Column(db.String(20))
    price = db.Column(db.String(20))
    user_token = db.Column(db.String, db.ForeignKey("user.token"), nullable=False)

    def __init__(self,doors,seats,make,model,series,year,color,price,user_token,id=""):
        self.doors = doors
        self.seats = seats
        self.make = make
        self.model = model
        self.series = series
        self.year = year
        self.color = color
        self.price = price
        self.user_token = user_token
        self.id = self.set_id()

    def __repr__(self):
        return f"Car: {self.year} {self.color} {self.make} {self.model} has been added!"
    
    def set_id(self):
        return (secrets.token_urlsafe())

class CarSchema(ma.Schema):
    class Meta:
        fields = ["id", "doors", "seats", "make", "model", "series", "year", "color", "price"]

car_schema = CarSchema()
cars_schema = CarSchema(many=True)