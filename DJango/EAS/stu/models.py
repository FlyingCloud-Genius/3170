from django.db import models
from reg.models import RegInfo
from uni.models import University

# Create your models here.
class Student(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=15)
    stu_name = models.CharField(max_length=40)    
    stu_email = models.CharField(max_length=30)
    stu_gender = models.IntegerField(blank=True, null=True)
    stu_birthday = models.DateField(blank=True, null=True)
    stu_major = models.CharField(max_length=50, blank=True, null=True)
    stu_c_uni = models.CharField(max_length=50, blank=True, null=True)
    reg = models.ForeignKey(RegInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student'


class StuPhones(models.Model):
    stu_phone = models.CharField(primary_key=True, max_length=20)
    stu = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stu_phones'
        unique_together = (('stu_phone', 'stu'),)


class StuInterests(models.Model):
    stu_interest = models.CharField(max_length=30, primary_key=True)
    stu = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stu_interests'
        unique_together = (('stu', 'stu_interest'),)


class StuApplication(models.Model):
    stu_app_id = models.CharField(primary_key=True, max_length=15)
    stu_resume = models.CharField(max_length=100)
    transcript = models.CharField(max_length=100)
    recommendation = models.CharField(max_length=50, blank=True, null=True)
    paper_title = models.CharField(max_length=100, blank=True, null=True)
    conference = models.CharField(max_length=50, blank=True, null=True)
    other_comments = models.CharField(max_length=50, blank=True, null=True)
    paper_url = models.CharField(max_length=100, blank=True, null=True)
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
