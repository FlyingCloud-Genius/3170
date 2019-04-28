from django.db import models
from reg.models import RegInfo

# Create your models here.
class Guardian(models.Model):
    guardian_id = models.CharField(primary_key=True, max_length=15)
    guardian_email = models.CharField(max_length=30, blank=True, null=True)
    guardian_fname = models.CharField(max_length=20, blank=True, null=True)
    guardian_lname = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    reg = models.ForeignKey(RegInfo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guardian'


# class Guard(models.Model):
#     guardian = models.ForeignKey('Guardian', models.DO_NOTHING, primary_key=True)
#     exam = models.ForeignKey(GreExam, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'guard'
#         unique_together = (('guardian', 'exam'),)