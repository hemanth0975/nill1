from django.db import models

# Create your models here.
class Student(models.Model):                                    # "Student" is a table name
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    mobile = models.IntegerField()
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name