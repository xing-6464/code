from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required

from forms.user import RegisterForm, LoginForm
from models.user import db, User

login_manager = LoginManager()

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

app = Flask(__name__)
# 设置配置文件
app.config.from_object('config')
# 添加数据库插件
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = '请先登录或注册'
# 创建数据库
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('sm.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(account_number=form.account_number.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        else:
            print('账号不存在或者密码错误')
        return redirect('index')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect('login', code=302)
    else:
        print(form.errors)
    return render_template('register.html')

@app.route('/share')
@login_required
def share():
    return render_template('share.html')

@app.route('/hdsc')
@login_required
def hdsc():
    return render_template('hdsc.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9521)
