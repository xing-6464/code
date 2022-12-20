// 商品价格
const goods = {
    '苹果': 6,
    '牛奶': 3.5,
    '面包': 5,
    '杯子': 24,
    '自行车': 360,
    '书包': 99.9,
    '鲜花': 49.9,
    '雨伞': 29.9
}
// 购物车数据
let goodsList = []

// 获取添加按钮dom
const li = document.querySelectorAll('li')

for (let i = 0; i < li.length; i++) {
    li[i].children[3].onclick = () => {
        const tr = document.createElement('tr')
        const tbody = document.querySelector('tbody')
        let html
        const goodsDate = {
            'name': li[i].querySelector('p').innerText,
            'count': 1
        }

        // 判断商品是否存在
        for (let i = 0; i < tbody.children.length; i++) {
            let tr = tbody.children[i]
            let tds = tr.querySelectorAll('td')
            let title = tds[0].innerText

            if (title === goodsDate.name) {
                // 改变购物车商品数量
                let ElementNum = tds[2].querySelector('span.cart-num')
                goodsList[i].count += 1
                
                ElementNum.innerText = goodsList[i].count
                // tds[1].innerHTML = `<td>￥${parseFloat(parseFloat(goods[goodsDate.name]) * goodsList[i].count).toFixed(2)}</td>`          
                totalMoney()
                return
            }

        }
        // 构造商品数据
        html = `
            <td>${goodsDate.name}</td>
            <td>￥${goods[goodsDate.name]}</td>
            <td>
                <span class="cart-num">1</span>
                <button class="delete" onclick="del(this)">x</button>
            </td>
        `
        goodsList.push(goodsDate)
        tr.innerHTML = html
        tbody.append(tr)

        // 计算价格总和
        totalMoney()
    }
}

// 计算价格总和
function totalMoney() {
    const tbody = document.querySelector('tbody')
    const p = document.querySelector('p.cart-totalLine')
    let html
    let money = 0
    
    goodsList.forEach(data => {
        money += parseFloat(parseFloat(goods[data.name]) * data.count)
    })

    html = `总计：<span>${money.toFixed(2)}</span>`

    p.innerHTML = html
}

// 删除逻辑
function del (btn) {
    const tbody = document.querySelector('tbody')
    const money = document.querySelector('p.cart-totalLine')
    const goodsName = btn.parentNode.parentNode.children[0].innerText
    
    // 当只有一件商品时
    if (goodsList.length === 1) {
        goodsList = []
        tbody.innerHTML = ''
        money.innerHTML = ''
        return
    }
    tbody.innerHTML = ''

    for (let i = 0; i < goodsList.length; i++) {
        if (goodsList[i].name === goodsName) {
            goodsList.splice(i, 1)
        }
    }

    for (let i = 0; i < goodsList.length; i++) {
        let tr = document.createElement('tr')
        // <td>￥${parseFloat(parseFloat(goods[goodsList[i].name]) * goodsList[i].count).toFixed(2)}</td>
        let html = `
            <td>${goodsList[i].name}</td>
            <td>￥${goods[goodsList[i].name]}</td>
            <td>
                <span class="cart-num">${goodsList[i].count}</span>
                <button class="delete" onclick="del(this)">x</button>
            </td>
        `

        tr.innerHTML = html
        tbody.appendChild(tr)
    }

    totalMoney()
}
