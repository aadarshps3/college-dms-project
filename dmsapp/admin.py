from django.contrib import admin

from dmsapp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Notification)
admin.site.register(models.Attendance)
