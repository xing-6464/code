from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import relationship
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    account = Column(String(15), nullable=False)
    password = Column(String(16), nullable=False)
    # personalInfo = relationship('PersonalInfo')
    # pid = Column(Integer, ForeignKey('personalInfo.id'))

    def check_password(self, password):
        return self.password == password

class PersonalInfo(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    email = Column(String(16), nullable=False)
    tall = Column(Integer, nullable=False)
    threeD = Column(String(20), nullable=False)
    workExperience = Column(String(1000), nullable=False)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

