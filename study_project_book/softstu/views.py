import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book

def get_books(request):
    books = Book.objects.all().values('book_id', 'title', 'author', 'price')
    return JsonResponse({"code": 200, "data": list(books)})

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