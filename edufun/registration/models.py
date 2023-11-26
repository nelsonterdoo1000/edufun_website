from django.db import models

# Create your models here.

class Trainee(models.Model):
    
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    phone = models.IntegerField(default=None)
    message = models.CharField(max_length=255)
    def __str__(self):
        return self.lname + ' ' +  self.fname 