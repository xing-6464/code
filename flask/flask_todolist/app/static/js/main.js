{/* <tr class="row">
    <td class="col-2"></td>
    <td class="col-7">
        <p></p>
        <input v-else v-model="editInput"  class="w-75 border border-white rounded-3" />
    </td>
    <td class="col-3">
        <button class="border border-white rounded-3 ms-2">完成</button>
        <button class="border border-white rounded-3 ms-2">保存</button>
        <button class="border border-white rounded-3 ms-2">删除</button>
    </td>
</tr> */}

// 列表渲染函数
function render (data, count) {
    // 初始化插入html
    let html = ''
    let all = count
    let success = 0
    console.log(data)
    // 遍历列表数据
    data.forEach((value, index) => {
        html += '<tr class="row table-success">'

        // 列表第一个条目
        html += `<td class="col-2">${ index + 1 }</td>`

        // 列表第二个条目
        html += '<td class="col-7">'
        // 判断是否是修改状态
        if (value.isEdit) {
            html += `<input id="editInput" value=${value.title} class="w-75 border border-white rounded-3" />`
        } else {
            if (value.isDone) {
                success += 1
                html += `<span class="done">${ value.title }</span>`
            } else {
                html += `<span>${ value.title }</span>`
            }
        }
        html += '</td>'

        // 第三个条目
        html += '<td class="col-3">'
        html += `<button id="Done${value.ID}-${value.isDone}" onclick="handleDone(id)" class="border border-white rounded-3 ms-2">${ value.isDone ? '开始' : '完成' }</button>`
        if (value.isEdit) {
            html += `<button id="save${value.ID}" onclick=handleSave(id) class="border border-white rounded-3 ms-2">保存</button>`
        } else {
            html += `<button id="edit${value.ID}" onclick=handleEdit(id) class="border border-white rounded-3 ms-2">编辑</button>`
        }
        html += `<button id="remove${value.ID}" onclick=handleRemove(id) class="border border-white rounded-3 ms-2">删除</button>`
        html += '</td>'
        html += '</tr>'
    })
    // 把列表展示到页面
    $('#showList').html(html)

    // 统计任务
    totalList(all, success)
}

// 抽象请求函数
function viewRequest (_url, method, _data=undefined) {
    $.ajax({
		url: "http://127.0.0.1:9521/todolist/ajax" + _url,
		dataType : "json",  // 数据格式
		type : method,      // 请求方式
		async : false,      // 是否异步请求
		data: _data,        // 传入数据
		success: function (res) { // 请求成功，返回数据
			render(res.data, res.count)
		}
	})
}

// 初始加载数据
$(document).ready(
    viewRequest('', 'get')
)

// 添加任务
function addList() {
    const addInput = document.querySelector('.addInput')
    if (addInput.value.trim()) {
        const data = {}
        data['title'] = addInput.value
        res = viewRequest('', 'post', data)
    }
    addInput.value = ''
}

// 删除任务
function handleRemove(id) {
    const removeId = id.substr(6)
    console.log(removeId)
    viewRequest(`?id=${removeId}`, 'delete')
}

// 修改任务完成情况
function handleDone(id) {
    const doneArr = id.substr(4).split('-')
    viewRequest(`/Done?id=${doneArr[0]}&isDone=${doneArr[1]}`, 'put')
}

// 修改任务信息
function handleEdit(id) {
    const editId = id.substr(4)
    viewRequest(`/Edit?id=${editId}`, 'put')
}

// 保存修改信息
function handleSave(id) {
    const saveID = id.substr(4)
    const editInput = document.getElementById('editInput')

    viewRequest(`/Save?id=${saveID}&title=${editInput.value.trim()}`, 'put')
}

// 搜索任务
function handleSearch() {
    const searchInput = document.getElementById('searchInput')
    const searchBtn = document.getElementById('searchBtn')
    const data = {}
    data['query'] = searchInput.value.trim()
    if (data.query) {
        viewRequest('/query', 'get', data)
    } else {
        viewRequest('', 'get')
    }
}

// 计算任务
function totalList(all, success) {
    document.querySelector('.all-list').innerText = `所有任务${ all ? all : '' }`
    document.querySelector('.success-list').innerText = `完成任务${ success ? success : '' }`
    document.querySelector('.handing-list').innerText = `进行中${ all - success ? all - success : '' }`
}
