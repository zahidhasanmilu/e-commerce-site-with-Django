from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'age')    
admin.site.register(Employee, EmployeeAdmin)