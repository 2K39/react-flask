from backend import db
from dataclasses import dataclass
from flask_login import UserMixin

@dataclass
class Admin(db.Model , UserMixin):
    id:int
    username:str
    password:str
    
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String , unique=True)
    password = db.Column(db.LargeBinary)



@dataclass
class User(db.Model):
    id:int
    username:str
    password:str
    
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String , unique=True)
    password = db.Column(db.String)