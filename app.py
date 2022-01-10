from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from security import authenticate, identity

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # creates a new endpoint, /auth where the username and password gets sent then gets it from security.py 

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__== '__main__' :
    db.init_app(app)
    app.run(port=5000, debug=True)