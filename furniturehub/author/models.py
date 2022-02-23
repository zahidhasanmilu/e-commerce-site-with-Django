from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(auto_created=True, primary_key=True)
    emp_name = models.CharField(max_length=30, null=False, blank=False)
    age = models.SmallIntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.emp_name