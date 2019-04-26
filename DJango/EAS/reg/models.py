from django.db import models

# Create your models here.

# class Info(models.Model):
#     reg_id = models.CharField(max_length = 30, primary_key = True)
#     reg_password = models.CharField(max_length = 16)

#     def __str__(self):
#         return self.reg_id

 
class RegInfo(models.Model):
    reg_id = models.CharField(max_length=30, primary_key=True)
    reg_password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'reg_info'