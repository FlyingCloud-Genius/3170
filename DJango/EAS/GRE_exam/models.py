from django.db import models

# Create your models here.
class GreExam(models.Model):
    exam_id = models.CharField(primary_key=True, max_length=15)
    exam_location = models.CharField(max_length=100, blank=True, null=True)
    exam_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GRE_exam'