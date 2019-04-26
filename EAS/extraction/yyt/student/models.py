from django.db import models
from reg.models import Info

# Create your models here.
class student(models.Model):
    stu_id = models.CharField(max_length = 15, primary_key = True)
    stu_email = models.CharField(max_length = 40, null = False)
    stu_name = models.CharField(max_length = 40, null = False)
    stu_photo = models.CharField(max_length = 100, null = True)
    stu_c_uni = models.CharField(max_length = 50, null = True)
    stu_major = models.CharField(max_length = 50, null = True)
    stu_gender = models.IntegerField(null = True)
    stu_birthday = models.DateField(null = True)
    reg_id = models.ForeignKey('Info', on_delete = models.CASCADE)


class phones(models.Model):
    stu_id = models.ForeignKey('student', on_delete = models.CASCADE)
    stu_phone =models.CharField(max_length = 20)

    class Meta:
        unique_together = (('stu_id', 'stu_phone'),)