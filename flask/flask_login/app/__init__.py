from flask import Flask
from flask_login import LoginManager

from app.web import web
from app.models.user import db, User

login_manager = LoginManager()

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.register_blueprint(web)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.index'

    with app.app_context():
        db.create_all()

    return app
    