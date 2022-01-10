from werkzeug.security import safe_str_cmp #safe string compare just to be
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity'] #part of Flask-JWT
    return UserModel.find_by_id(user_id)