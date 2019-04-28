from django.db import models
from reg.models import RegInfo
from uni.models import University

# Create your models here.
class Student(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=15)
    stu_fname = models.CharField(max_length=20, blank=True, null=True)
    stu_lname = models.CharField(max_length=20, blank=True, null=True)
    stu_phone = models.CharField(max_length=20, blank=True, null=True)
    stu_gender = models.IntegerField(blank=True, null=True)
    stu_major = models.CharField(max_length=50, blank=True, null=True)
    stu_email = models.CharField(max_length=30, blank=True, null=True)
    stu_c_uni = models.CharField(max_length=50, blank=True, null=True)
    reg = models.ForeignKey(RegInfo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StuApplication(models.Model):
    stu_app_id = models.CharField(primary_key=True, max_length=15)
    stu_resume = models.CharField(max_length=100, blank=True, null=True)
    transcript = models.CharField(max_length=100, blank=True, null=True)
    recommendation = models.CharField(max_length=50, blank=True, null=True)
    stu = models.ForeignKey('Student', models.DO_NOTHING)
    apply_uni = models.ForeignKey(University, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stu_application'


class StuDreamMajors(models.Model):
    stu_dream_major = models.CharField(max_length=20)
    stu_app = models.ForeignKey(StuApplication, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'stu_dream_majors'
        unique_together = (('stu_app', 'stu_dream_major'),)
