import math

from flask import current_app, jsonify

from app.util import database_to_dict
from app.models.todoList import TodoListModel, db

class TodoListController(TodoListModel):

    # 为数据库添加一条数据
    @classmethod
    def add_list(cls, dict):
        try:
            todo_list = TodoListModel(title=dict['title'])
            print(todo_list.isDone)
            db.session.add(todo_list)
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
        return  cls.get_all()

    # 获取数据库数据
    @classmethod
    def get_all(cls):
        # 获取数据库全部信息
        database = TodoListModel.query.all()
        count = len(database)
        # 遍历数据库数据生成我们的数据结构
        data = database_to_dict(database)
        # print(data)
        
        return { 'code': 200, 'msg': '获取数据成功', 'data': data, 'count': count }

    # 删除数据库一条数据
    @classmethod
    def remove_list(cls, id):
        try:
            TodoListModel.query.filter(TodoListModel.ID == id).delete()
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
        return cls.get_all()

    # 是否完成任务功能
    @classmethod
    def done_list(cls, id, isDone):
        try:
            TodoListModel.query.filter(TodoListModel.ID == id).update({'isDone': not isDone})
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
        return cls.get_all()
    
    # 重新编辑任务
    @classmethod
    def edit_list(cls, id):
        try:
            TodoListModel.query.filter(TodoListModel.ID == id).update({'isEdit': True})
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
        return cls.get_all()
    
    # 保存重新编辑数据
    @classmethod
    def save_list(cls, id, title):
        try:
            TodoListModel.query.filter(TodoListModel.ID == id).update({'isDone': False, 'isEdit': False, 'title': title})
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
        return cls.get_all()
    
    # 查询数据库, 模糊查询
    @classmethod
    def search_list(cls, query):
        try:
            search_list = []
            database_search_list = TodoListModel.query.filter(TodoListModel.title.contains(query)).all()
            count = len(TodoListModel.query.all())
            if len(database_search_list):
                search_list = database_to_dict(database_search_list)
            else:
                search_list = []
        except Exception as e:
            print(e)
        finally:
            db.session.close()
        return { 'code': 200, 'msg': '查询数据成功', 'data': search_list, 'count': count }
