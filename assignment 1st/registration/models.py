from django.db import models


# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self


class employeekin(models.Model):
    full_name = models.CharField(max_length=30)
    employee_name = models.CharField(max_length=30)
    ID_no = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name
