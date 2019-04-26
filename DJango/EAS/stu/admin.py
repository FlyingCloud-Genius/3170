from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Student)
admin.site.register(models.StuPhones)
admin.site.register(models.StuInterests)
admin.site.register(models.StuDreamMajors)
admin.site.register(models.StuApplication)
