from wtforms import Form, StringField, PasswordField, ValidationError
from wtforms.validators import Length, DataRequired

from models.user import User

class RegisterForm(Form):
    account_number = StringField(validators=[DataRequired(), Length(3, 64)])
    password = PasswordField(validators=[DataRequired(message='密码不能为空，请输入你的密码'), Length(6, 32)])
    address = StringField(validators=[DataRequired(), Length(0, 10)])

    def validate_account_number(self, field):
        if User.query.filter_by(account_number=field.data).first():
            raise ValidationError('用户已被注册')

class LoginForm(Form):
    account_number = StringField(validators=[DataRequired(), Length(3, 64)])
    password = PasswordField(validators=[DataRequired(message='密码不能为空，请输入你的密码'), Length(6, 32)])
    