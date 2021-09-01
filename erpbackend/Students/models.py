from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=140)
    Course = models.CharField(max_length=140)
    Rating = models.IntegerField()
    def __str__(self):
        return self.Name

class Meta:
    ordering = ['Name']
