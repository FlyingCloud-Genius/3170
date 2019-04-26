from django.db import models
from reg.models import RegInfo

# Create your models here.
class University(models.Model):
    uni_id = models.CharField(primary_key=True, max_length=15)
    uni_email = models.CharField(max_length=30)
    uni_name = models.CharField(max_length=100)
    uni_phone = models.CharField(max_length=20)
    required_gre_score = models.IntegerField(db_column='required_GRE_score', blank=True, null=True)  # Field name made lowercase.
    uni_address = models.CharField(max_length=100, blank=True, null=True)
    reg = models.ForeignKey(RegInfo, models.DO_NOTHING)

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