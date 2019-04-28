from django.db import models
from reg.models import RegInfo
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your models here.
class University(models.Model):
    uni_id = models.CharField(primary_key=True, max_length=15)
    uni_email = models.CharField(max_length=30, blank=True, null=True)
    uni_name = models.CharField(max_length=100, blank=True, null=True)
    uni_phone = models.CharField(max_length=20, blank=True, null=True)
    required_score = models.IntegerField(blank=True, null=True)
    reg = models.ForeignKey(RegInfo, models.DO_NOTHING, blank=True, null=True)
    uni_web = models.CharField(max_length=100, blank=True, null=True)
    uni_photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university'

class UniOpenMajor(models.Model):
    open_major = models.CharField(max_length=50)
    enrollment = models.IntegerField(blank=True, null=True)
    uni = models.ForeignKey('University', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'uni_open_major'
        unique_together = (('uni', 'open_major'),)


# class StuApplication(models.Model):
#     stu_app_id = models.CharField(primary_key=True, max_length=15)
#     stu_resume = models.CharField(max_length=100, blank=True, null=True)
#     transcript = models.CharField(max_length=100, blank=True, null=True)
#     recommendation = models.CharField(max_length=50, blank=True, null=True)
#     paper_title = models.CharField(max_length=100, blank=True, null=True)
#     conference = models.CharField(max_length=50, blank=True, null=True)
#     other_comments = models.CharField(max_length=50, blank=True, null=True)
#     paper_url = models.CharField(max_length=100, blank=True, null=True)
#     stu = models.ForeignKey(Student, models.DO_NOTHING)
#     apply_uni = models.ForeignKey('University', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'stu_application'
