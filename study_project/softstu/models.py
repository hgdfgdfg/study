from django.db import models

class Student(models.Model):
    stuId = models.CharField(db_column='stuId', max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'student'  
        # 已经删除了 managed = False，重新把建表权交还给 Django！