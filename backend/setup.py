from hashlib import new
from operator import ne
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
from flask_jwt_extended import JWTManager
from datetime import timedelta



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

env = environ.get("ENVIRONMENT", "development")

# instantiate secrets and env variables
app.config['SECRET_KEY'] = 'c1155c6a351e49eba15c00ce577b259e'

setup = False
if not path.isfile("db.sqlite3"):
    open("db.sqlite3", "w")
    setup = True

if env == "development":
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3" # Declares the database path
else:
    # add production database
    username = environ.get("DB_USERNAME")
    password = environ.get("DB_PASSWORD")
    host = environ.get("DB_HOST")
    database = environ.get("DB_DATABASE")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@{host}:5432/{database}" # Declares the database path

# instantiate the db   
db = SQLAlchemy(app)

jwt = JWTManager(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


from models import *

db.create_all()







##### Comment add un user
from models import *

usertest = user.User.query.all() 
if len(usertest) == 0 :
    newUserPseudo = user.User("pseudo","mdp",False,2)
    db.session.add(newUserPseudo)
    db.session.commit()
    newUser = user.User("PGM","mdp",False,100)
    newUser.elo = 2000
    db.session.add(newUser)
    db.session.commit()
    newUser = user.User("SemiPro","mdp",False,75)
    newUser.elo = 1000
    db.session.add(newUser)
    db.session.commit()
    newUser = user.User("LeTiroir","mdp",False,30)
    db.session.add(newUser)
    db.session.commit()
    newUser = user.User("MecPasOuf","mdp",False,10)
    newUser.elo = 500
    db.session.add(newUser)
    db.session.commit()
    
##### 


##### Comment add une game normale 

from sqlalchemy.orm import with_polymorphic

all_games_poly = with_polymorphic(game.Game, [game_normal.Game_normal])

all_games = db.session.query(all_games_poly)
if len(all_games.all()) == 0 :

    user_id = newUserPseudo.id       # Juste pour récupérer un user, sinon remplacer par ce qu'il vous faut

    newGameNormal = game_normal.Game_normal(user_id,"TENDRESSE",7,9)       
    db.session.add(newGameNormal)
    newGameId = newGameNormal.id
    newGameNormal.state = True
    db.session.add(tries.Tries(newGameId,"COMBATIVE",1))
    db.session.add(tries.Tries(newGameId,"JUGEMENTS",2))
    db.session.add(tries.Tries(newGameId, "TENDRESSE",3))

    newGameNormal = game_normal.Game_normal(user_id,"AMOUR",6,5)       
    db.session.add(newGameNormal)
    newGameId = newGameNormal.id
    newGameNormal.state = True
    db.session.add(tries.Tries(newGameId,"AMOUR",1))
    
    

    newGameNormal = game_normal.Game_normal(user_id,"CHOCOLAT",4,8)       
    db.session.add(newGameNormal)
    newGameId = newGameNormal.id
    newGameNormal.state = True
    db.session.add(tries.Tries(newGameId,"AMAIGRIE",1))
    db.session.add(tries.Tries(newGameId, "CHIENNES",2))
    db.session.add(tries.Tries(newGameId, "CHAUFFER",3))
    db.session.add(tries.Tries(newGameId, "CHOISIES",4))

    db.session.commit()

    # newGameNormal = game_normal.Game_normal(user.id,"TESTER",3,6)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"B"*newGameNormal.length,int(2)))
    # db.session.add(tries.Tries(newGameId,"C"*newGameNormal.length,int(3)))

    # newGameNormal =game_normal.Game_normal(user.id,"TESTS",6,5)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"TESTS",int(2)))

    # newGameNormal =game_normal.Game_normal(user.id,"OKAY",4,4)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"B"*newGameNormal.length,int(2)))
    # db.session.add(tries.Tries(newGameId,"C"*newGameNormal.length,int(3)))
    # db.session.add(tries.Tries(newGameId,"D"*newGameNormal.length,int(4)))

    # newGameNormal =game_normal.Game_normal(user.id,"SALUT",3,5)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"B"*newGameNormal.length,int(2)))
    # db.session.add(tries.Tries(newGameId,"C"*newGameNormal.length,int(3)))

    # newGameNormal =game_normal.Game_normal(user.id,"MEC",6,3)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"B"*newGameNormal.length,int(2)))
    # db.session.add(tries.Tries(newGameId,"C"*newGameNormal.length,int(3)))
    # db.session.add(tries.Tries(newGameId,"D"*newGameNormal.length,int(4)))
    # db.session.add(tries.Tries(newGameId,"MEC",int(5)))


    # newGameNormal =game_normal.Game_normal(user.id,"CHIEN",3,5)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"B"*newGameNormal.length,int(2)))
    # db.session.add(tries.Tries(newGameId,"C"*newGameNormal.length,int(3)))

    # newGameNormal =game_normal.Game_normal(user.id,"BANANE",2,6)
    # db.session.add(newGameNormal)
    # newGameId = newGameNormal.id
    # db.session.add(tries.Tries(newGameId,"A"*newGameNormal.length,int(1)))
    # db.session.add(tries.Tries(newGameId,"B"*newGameNormal.length,int(2)))


    # Et comment add une game survie

    # newGameSurvie = game_survie.Game_survie(user.id,8,10)     
    # db.session.add(newGameSurvie)
    # db.session.commit()

#####






##### Comment récupérer toutes les games :


all_games_poly = with_polymorphic(game.Game, [game_normal.Game_normal,game_carriere.Game_carriere])

all_games = db.session.query(all_games_poly)

# first_game = all_games[0]

# date = first_game.date              #Pour récup la date
# state = first_game.state            #Pour récup le state
# id = first_game.id                  #Pour récup l'id
# game_type = first_game.game_type    #Pour récup le type de game

# if game_type == "game_normal" :

#     id_user = first_game.id_user    #Pour récup le user_id
#     solution = first_game.solution  #Pour récup la solution
#     maxtry = first_game.maxtry      #Pour récup le nb de try
#     length = first_game.length      #Pour récup la longeur de la soluce

##print(date,state,id,game_type,id_user,solution,maxtry,length)


# Récup les infos d'une game survie

# game_s = all_games[1]

# date = game_s.date              
# state = game_s.state            
# id = game_s.id                  
# game_type = game_s.game_type    

# if game_type == "game_survie" :

#     id_user = game_s.id_user    #Pour récup le user_id
#     maxtry = game_s.maxtry      #Pour récup le nb de try
#     length = game_s.length      #Pour récup la longeur des soluces
#     score = game_s.score

##print(solution,game_type,score,state)

########



