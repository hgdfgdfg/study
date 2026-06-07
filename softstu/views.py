from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

# 1. 查询全部学生接口
def get_students(request):
    students = Student.objects.all().values() # 查出所有学生
    return JsonResponse({"code": 200, "data": list(students)})

# 2. 增加学生接口
@csrf_exempt  # 临时免除CSRF Token认证，方便Axios测试
def add_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # 将前端传来的数据存入数据库
        Student.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            # ...其他字段
        )
        return JsonResponse({"code": 200, "msg": "添加成功"})