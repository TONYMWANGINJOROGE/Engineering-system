from django.db import models


# Create your models here.
class Employees(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    emp_code = models.CharField(max_length=5)
    MobileNumber = models.CharField(max_length=20)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
