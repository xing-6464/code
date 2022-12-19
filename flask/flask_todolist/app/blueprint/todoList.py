from flask import Blueprint
from flask import render_template, request

# from app.models.todoList import TodoListModel
from app.controller.todoList import TodoListController

# 初始化蓝图
todolist_views = Blueprint("todolist", __name__, url_prefix="/todolist")

# 渲染
@todolist_views.route('/')
def ajax():
    return render_template('todolist.html')

# 获取所有数据
@todolist_views.route('/ajax', methods=['GET'])
def ajaxAll():
    res = TodoListController.get_all()
    return res

# 添加一条数据
@todolist_views.route('/ajax', methods=['POST'])
def ajaxAdd():
    # 得到添加数据信息设置为可变字典
    ajaxData = request.form.to_dict()
    res = TodoListController.add_list(ajaxData)
    return res

# 删除一条数据
@todolist_views.route('/ajax', methods=['DELETE'])
def ajaxRemove():
    # 删除任务的ID
    id = request.args['id']
    res = TodoListController.remove_list(id)
    return res

# 修改任务，编辑，保存，完成
@todolist_views.route('/ajax/<param>', methods=['PUT'])
def ajaxPut(param):
    id = request.args['id']
    # print(request.args)
    if param == 'Done':
        # 因为JavaScript的boolean类型不一样需要转换
        isDone = False if request.args['isDone'] == 'false' else True
        res = TodoListController.done_list(id, bool(isDone))
        return res
    elif param == 'Edit':
        res = TodoListController.edit_list(id)
        return res
    elif param == 'Save':
        title = request.args['title']
        res = TodoListController.save_list(id, title)
        return res

# 查询数据库
@todolist_views.route('/ajax/query', methods=['GET'])
def getAjaxQeury():
    query = request.args['query']
    res = TodoListController.search_list(query)
    return res
