from django.db import models
from StudentApi import settings
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    SCHOOLS = [
    'SCI',
    'ENGINEERING',
    'SOBE',
    'SEDU',
    'PUBLIC HEALTH',
    'DEMA',
    ]


    DEPARTMENTS = [
    'Information Technology',
    'Computer Science',
    'Civil and Structural Engineering',
    'Elecctrical Engineering',
    'Optimetry and Vision Sciences',
    ]

    #user = models.ForeignKey('auth.User', related_name='students', on_delete=models.CASCADE, default=1)
    surname = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    last_nme = models.CharField(max_length = 100)
    id_number = models.IntegerField()
    email = models.EmailField()
    reg_number = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)

    def __str__(self):
        return self.reg_number
    
    class Meta:
        verbose_name_plural = 'Student'
    