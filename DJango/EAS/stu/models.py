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
    stu_resume = models.CharField(max_length=1000, blank=True, null=True)
    transcript = models.CharField(max_length=1000, blank=True, null=True)
    recommendation = models.CharField(max_length=1000, blank=True, null=True)
    stu_id = models.CharField(max_length=15)
    apply_uni_id = models.CharField(max_length=15)
    status = models.CharField(max_length=255)

    def as_dict(self):
        return {
            "stu_app_id":self.stu_app_id,
            "stu_resume":self.stu_resume,
            "transcript":self.transcript,
            "recommendation":self.recommendation,
            "stu_id":self.stu_id,
            "apply_uni_id":self.apply_uni_id,
            "status":self.status
        }

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

class StuExam(models.Model):
    exam_id = models.CharField(primary_key=True, max_length=15)
    exam_location = models.CharField(max_length=100)
    exam_time = models.TimeField()
    availability = models.IntegerField()

    def as_dict(self):
        smallDict = {0: "No", 1: "Yes"}
        return {
            "examid":self.exam_id,
            "examtime":self.exam_time.__str__(),
            "examcity":self.exam_location,
            "examavail":smallDict[self.availability]
        }

    class Meta:
        managed = False
        db_table = 'exam'

class StuExercise(models.Model):
    que_id = models.CharField(primary_key=True, max_length=15)
    que_analysis = models.CharField(max_length=1000, blank=True, null=True)
    difficulty_level = models.IntegerField(blank=True, null=True)
    que_content = models.CharField(max_length=1000, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    que_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_base'

    def as_dict(self):
        return {
            "ID":self.que_id,
            "analysis":self.que_analysis,
            "difficulty":self.difficulty_level,
            "content":self.que_content,
            "answer":self.answer,
            "type":self.que_type
        }
    

class AppliedExam(models.Model):
    stu_id = models.CharField(max_length=15)
    exam_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'attendance'

class StuAnswerSheet(models.Model):
    ans_id = models.CharField(primary_key=True, max_length=15)
    student_solution = models.CharField(max_length=1000)
    ans_score = models.CharField(max_length=4)
    examinee = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = "answer_sheet"
    
    def as_dict(self):
        flag = False
        if self.ans_score: flag = True
        return {
            "AnswerSheetID":self.ans_id,
            "Solution":self.student_solution,
            "checked":flag,
            "Score": self.ans_score,
            "examinee": self.examinee
        }