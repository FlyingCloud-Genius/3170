from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.University)
admin.site.register(models.UniOpenMajor)