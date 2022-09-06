from django.contrib import admin
from .models import employee
# Register your models here.
@admin.register(employee)
class employeeadmin(admin.ModelAdmin):
    list_display=['em_name','em_email','img','pdf']
