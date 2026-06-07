from django.contrib import admin
from django.urls import path
from softstu import views  # 引入我们刚才写的 views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 给前端提供的两个接口地址
    path('api/students/', views.get_students),
    path('api/students/add/', views.add_student),
]