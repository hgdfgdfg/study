import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book

# 1. 查询全部图书
def get_books(request):
    books = Book.objects.all().values('book_id', 'title', 'author', 'price')
    return JsonResponse({"code": 200, "data": list(books)})

# 2. 增加图书
@csrf_exempt  
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Book.objects.create(
            book_id=data.get('book_id'),
            title=data.get('title'),
            author=data.get('author'),
            price=data.get('price')
        )
        return JsonResponse({"code": 200, "msg": "添加成功"})

# 3. 删除图书 (新增)
@csrf_exempt
def delete_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = data.get('book_id')
        try:
            book = Book.objects.get(book_id=book_id)
            book.delete() # 从数据库彻底删除
            return JsonResponse({"code": 200, "msg": "图书删除成功"})
        except Book.DoesNotExist:
            return JsonResponse({"code": 404, "msg": "该图书不存在"})

# 4. 修改图书 (新增)
@csrf_exempt
def update_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = data.get('book_id')
        try:
            book = Book.objects.get(book_id=book_id)
            # 更新字段
            book.title = data.get('title')
            book.author = data.get('author')
            book.price = data.get('price')
            book.save() # 保存修改到数据库
            return JsonResponse({"code": 200, "msg": "图书修改成功"})
        except Book.DoesNotExist:
            return JsonResponse({"code": 404, "msg": "该图书不存在"})