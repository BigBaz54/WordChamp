from setup import *
from uuid import uuid4
from setup import db

class Tries(db.Model):
    __tablename__ = 'tries'
    id = db.Column(db.String(40), primary_key=True)
    try_number = db.Column(db.Integer,nullable=False)
    word = db.Column(db.String(40), nullable=False)
    id_game = db.Column(db.String(40), db.ForeignKey("games.id"),nullable=False)
    game_type = db.Column(db.String(40), db.ForeignKey("games.game_type"),nullable=False)

    def __init__(self, id_game,game_type,word,try_number):
        self.id = uuid4().hex
        self.id_game = id_game
        self.type = game_type
        self.word = word
        self.try_number = try_number

    def __repr__(self):
        return '<Tentative %r>' % self.word