new Vue({
    el: '#app',
    data: {
        activeView: 'display', 
        bookList: [],          
        bookCount: 0,          
        newBook: { book_id: '', title: '', author: '', price: '' },
        
        // --- 新增：用于修改功能的控制变量 ---
        isEditing: false, 
        editBookData: { book_id: '', title: '', author: '', price: '' },
        
        baseUrl: 'http://127.0.0.1:8000/api'
    },
    created() {
        this.findAll();
    },
    methods: {
        switchView(viewName) {
            this.activeView = viewName;
            // 每次切换页面时，都拉取一次最新数据，并隐藏可能开着的修改表单
            this.findAll();
            this.isEditing = false; 
        },

        // 查询
        findAll() {
            axios.get(`${this.baseUrl}/books/`)
                .then(response => {
                    if (response.data.code === 200) {
                        this.bookList = response.data.data;
                        this.bookCount = this.bookList.length;
                    }
                })
        },

        // 增加
        addBook() {
            axios.post(`${this.baseUrl}/books/add/`, this.newBook)
                .then(response => {
                    if (response.data.code === 200) {
                        alert("✅ 图书录入成功！");
                        this.newBook = { book_id: '', title: '', author: '', price: '' };
                        this.findAll();
                        this.switchView('display');
                    } else {
                        alert("添加失败：" + response.data.msg);
                    }
                })
        },

        // 删除功能 (新增)
        deleteBook(book_id) {
            // 弹窗让用户二次确认，防止手滑
            if (!confirm("⚠️ 危险操作！确定要彻底删除编号为 [" + book_id + "] 的图书吗？")) {
                return;
            }
            axios.post(`${this.baseUrl}/books/delete/`, { book_id: book_id })
                .then(response => {
                    if (response.data.code === 200) {
                        alert("🗑️ " + response.data.msg);
                        this.findAll(); // 删除成功后自动刷新表格
                    } else {
                        alert(response.data.msg);
                    }
                })
        },

        // 修改功能 1：点击"编辑"按钮，弹出表单并填充数据 (新增)
        startEdit(item) {
            this.isEditing = true;
            // 把当前选中的行数据，拷贝一份给编辑表单
            this.editBookData = {
                book_id: item.book_id,
                title: item.title,
                author: item.author,
                price: item.price
            };
            // 页面平滑滚动到表单顶部
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        // 修改功能 2：取消编辑，收起表单 (新增)
        cancelEdit() {
            this.isEditing = false;
            this.editBookData = { book_id: '', title: '', author: '', price: '' };
        },

        // 修改功能 3：保存提交修改后的数据到后端 (新增)
        saveUpdateBook() {
            axios.post(`${this.baseUrl}/books/update/`, this.editBookData)
                .then(response => {
                    if (response.data.code === 200) {
                        alert("✏️ " + response.data.msg);
                        this.isEditing = false; // 保存成功后收起表单
                        this.findAll();         // 刷新表格看最新数据
                    } else {
                        alert(response.data.msg);
                    }
                })
        }
    }
});