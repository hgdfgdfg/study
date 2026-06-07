import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

# 任务一：查询全部学生
def get_students(request):
    # 从 SQL Server 数据库中查出所有的学生数据
    students = Student.objects.all().values('stuId', 'name', 'age')
    return JsonResponse({"code": 200, "data": list(students)})

# 任务二：接收前端传来的数据并增加学生
@csrf_exempt  # 暂时免除跨域令牌验证，方便调试
def add_student(request):
    if request.method == 'POST':
        # 解析前端发来的 JSON 数据
        data = json.loads(request.body)
        # 将数据保存到 SQL Server 数据库中
        Student.objects.create(
            stuId=data.get('stuId'),
            name=data.get('name'),
            age=data.get('age')
        )
        return JsonResponse({"code": 200, "msg": "添加成功"})