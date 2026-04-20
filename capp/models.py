from capp import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Database User
class User(db.Model, UserMixin):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    transport = db.relationship('Transport', backref='author', lazy=True) #makes sure that the user can have multiple transport entries, and that we can access the user from the transport entry with "author"

# Database Transport
class Transport(db.Model):
    # __bind_key__ = 'transport' # This line is optional if you want to use a separate database for transport data --> does not work in our case
    __tablename__= 'transport_table'
    id = db.Column(db.Integer, primary_key=True)
    kms = db.Column(db.Float)
    transport = db.Column(db.String)
    fuel = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    co2= db.Column(db.Float)
    ch4= db.Column(db.Float)
    total = db.Column(db.Float)  
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    # db.ForeignKey('user_table.id') creates a foreign key relationship between the transport entry and the user who created it, allowing us to access the user from the transport entry with "author" (as defined in the User model)

# User registers → saved in user_table
# User logs a trip → saved in transport_table with their user_id
# User views dashboard → queries transport_table filtered by their user_id
# User deletes entry → removes that row from transport_table