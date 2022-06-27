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

class Review(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15,default='22-1 semester')
    assignment = models.CharField(max_length=10)
    groupmeeting = models.CharField(max_length=10)
    grade = models.CharField(max_length=15)
    attendence = models.CharField(max_length=15)
    numberoftests = models.CharField(max_length=15)
    body = models.TextField(default='내용')
    