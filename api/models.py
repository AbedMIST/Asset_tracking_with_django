from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    condition = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    #assigned_to = models.CharField(max_length=100)
    assigned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

