from django.db import models
from django.conf import settings
class Semester(models.Model):
    name = models.CharField(max_length=100)
    
class Table(models.Model):
    name = models.CharField(max_length=200)

class Class(models.Model):
    major = models.CharField(max_length=15, default='교양')
    credit = models.IntegerField(default=2, null=True)
    name = models.CharField(max_length=200)
    professor = models.CharField(max_length=20)
    day = models.CharField(max_length=3)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=20, null=True)
    class_id = models.CharField(max_length=10, primary_key=True)

