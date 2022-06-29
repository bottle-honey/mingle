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
    def __str__(self):
        return self.class_id
class Review(models.Model):
    semester_values = [('1','21-1'), ('2','21-2'), ('3','22-1')]
    groupmeeting_values = [('1','Many'),('2','Normal'),('3','None')]
    assignment_values = [('1','Many'),('2','Normal'),('3','None')]
    grade_values = [('1','Genorosity'),('2','Mediocrity'),('3','Strictness')]
    attendendce_values = [('1','Mixed'),('2','Direct name'),('3','Designated seat'),('4','Electronic attendence')]
    numberoftest_values = [('1','0'),('2','1'),('3','2'),('4','3'),('5','4+')]
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    assignment = models.CharField(choices=groupmeeting_values,default='3',max_length=5)
    groupmeeting = models.CharField(choices=assignment_values,default='3',max_length=5)
    grade = models.CharField(choices=grade_values,default='1',max_length=10)
    attendence = models.CharField(choices=attendendce_values,default='1',max_length=21)
    numberoftests = models.CharField(choices=numberoftest_values,default='1',max_length=2)
    semester = models.CharField(choices=semester_values, default='3', max_length=4)
    body = models.TextField(default='')
    