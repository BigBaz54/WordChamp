from setup import *
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import os
import json

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def is_admin(self):
        return self.admin
    
    def avatar_name(self):
        folder = f"static/avatar/{self.id}"
        if not os.path.exists(folder):
            return "0"
        L = os.listdir(folder)
        if len(L) == 0: 
            return "0"
        name = L[0].replace(".png", "")
        return name
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password, admin=False):
        self.id = uuid4().hex
        self.username = username
        self.set_password(password)
        self.admin = admin

    def __repr__(self):
        return '<User %r>' % self.username

    def toDict(self):
        dictionnaire = {}
        dictionnaire['id']=self.id
        dictionnaire['username']=self.username
        dictionnaire['password_hash']=self.password_hash
        return dictionnaire
