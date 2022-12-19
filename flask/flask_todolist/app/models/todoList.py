import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 定义todoList对象
class TodoListModel(db.Model):
    # 表名
    __tablename__ = 'todoList'

    # 表的结构
    ID = Column(Integer, primary_key=True, autoincrement=True, info='ID')
    title = Column(String(50), info='任务')
    isEdit = Column(Boolean, default=False, info='是否修改')
    isDone = Column(Boolean, default=False, info='是否完成任务')
    createTime = Column(DateTime, default=datetime.datetime.now, index=True, info='记录添加时间')
