from django.contrib import admin
from django.urls import path
from softstu import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', views.get_books),
    path('api/books/add/', views.add_book),
    path('api/books/delete/', views.delete_book),
    path('api/books/update/', views.update_book),
]