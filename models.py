from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta
import uuid

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20))
    country = db.Column(db.String(50), default='Nigeria')
    is_subscribed = db.Column(db.Boolean, default=False)
    subscription_expires = db.Column(db.DateTime, nullable=True)
    payment_provider = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_id = db.Column(db.String(20), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    courier_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    pickup_address = db.Column(db.String(255), nullable=False)
    dropoff_address = db.Column(db.String(255), nullable=False)
    pickup_lat = db.Column(db.Float, nullable=True)
    pickup_lng = db.Column(db.Float, nullable=True)
    dropoff_lat = db.Column(db.Float, nullable=True)
    dropoff_lng = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text)
    weight = db.Column(db.Float)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), default='NGN')
    status = db.Column(db.String(30), default='pending')
    commission_rate = db.Column(db.Float, default=0.10)
    commission_amount = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    customer = db.relationship('User', foreign_keys=[customer_id], backref='customer_deliveries')
    courier = db.relationship('User', foreign_keys=[courier_id], backref='courier_deliveries')

def generate_tracking_id():
    return 'DLV-' + str(uuid.uuid4())[:8].upper()
