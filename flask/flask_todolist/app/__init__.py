from flask import Flask

from app.blueprint.todoList import todolist_views
from app.models.todoList import db


def create_app():
    # 创建flask实例，并且配置静态文件
    app = Flask(__name__, template_folder='./templates', static_folder="./static")

    # 创建配置文件
    app.config.from_object('app.config')

    # db绑定app
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # 插入蓝图
    app.register_blueprint(todolist_views)

    return app
