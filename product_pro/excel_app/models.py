from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade_level = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')

class Class(models.Model):
    name = models.CharField(max_length=100)
    schedule_time = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='subjects')
