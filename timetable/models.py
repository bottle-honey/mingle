from django.db import models
from django.conf import settings
class Semester(models.Model):
    name = models.CharField(max_length=100)
    
class Table(models.Model):
    name = models.CharField(max_length=200)

class Class(models.Model):
    name = models.CharField(max_length=200)
    professor = models.CharField(max_length=20)
    day = models.CharField(max_length=5)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    classroom = models.CharField(max_length=20)
    class_id = models.IntegerField(primary_key=True)