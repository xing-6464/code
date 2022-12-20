from flask import render_template, request, redirect
from flask_login import login_required, login_user

from app.web import web
from app.models.user import db, User, PersonalInfo


@web.route('/', methods=['GET', 'POST'])
def index():
    form = request.form.to_dict()
    if request.method == 'POST':
        user = User.query.filter_by(account=form['account']).first()
        if user and user.check_password(form['password']):
            login_user(user)
            return redirect('user')
        else:
            print('账号不存在或者密码错误')
    return render_template('index.html')

@web.route('/mi')
def mi():
    return render_template('MI.html')

@web.route('/us', methods=['GET', 'POST'])
@login_required
def us():
    form = request.form.to_dict()
    print(form)
    if request.method == 'POST':
        personal_info = PersonalInfo()
        personal_info.set_attrs(form)
        db.session.add(personal_info)
        db.session.commit()
    return render_template('us.html')

@web.route('/user')
@login_required
def user():
    return render_template('user.html')
