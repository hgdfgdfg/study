new Vue({
    el: '#app', // 极其精准挂载到你原版的页面大包裹盒，确保全响应式布局完全不崩
    data: {
        activeView: 'display', // 默认高亮并激活“图书显示”
        bookList: [],          // 用来装从你本地 Django 数据库查到的动态图书数组
        bookCount: 0,          // 绑定总数
        newBook: {             // 录入表单绑定对象
            book_id: '',
            title: '',
            author: '',
            price: ''
        },
        baseUrl: 'http://127.0.0.1:8000/api' // 指向你自己运行的 Django 本地服务地址
    },
    created() {
        // 页面刚渲染好，主动请求后端并获取全部图书
        this.findAll();
    },
    methods: {
        // 丝滑控制左侧导航菜单的高亮状态切换
        switchView(viewName) {
            this.activeView = viewName;
        },

        // 功能点一：查询全部图书数据并实时更新至表格
        findAll() {
            axios.get(`${this.baseUrl}/books/`)
                .then(response => {
                    // 假设后端返回规范格式 {"code": 200, "data": [...]}
                    if (response.data.code === 200) {
                        this.bookList = response.data.data;
                        this.bookCount = this.bookList.length;
                    }
                })
                .catch(error => {
                    console.log("提示：后端接口未开启或本地开发存在跨域拦截，暂时无法抓取最新图书表。");
                });
        },

        // 功能点二：增加新图书到你的后台数据库中
        addBook() {
            axios.post(`${this.baseUrl}/books/add/`, this.newBook)
                .then(response => {
                    if (response.data.code === 200) {
                        alert("图书录入成功！");
                        // 1. 清空输入框表单数据以供下次输入
                        this.newBook = { book_id: '', title: '', author: '', price: '' };
                        // 2. 重新跑一遍查询全部，将最新的数据库数据同步过来
                        this.findAll();
                        // 3. 点击完成录入，自动平滑切回图书数据显示视图
                        this.switchView('display');
                    } else {
                        alert("添加失败：" + response.data.msg);
                    }
                })
                .catch(error => {
                    alert("无法连接服务器，录入请求发送失败，请确保你的 Django 后台处于 Run 状态！");
                });
        }
    }
});