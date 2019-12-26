from django.db import models

# Create your models here.

GENDER = [('m', 'Male'), ('f', 'Female')]


class School(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=30)
    school_id = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=2, choices=GENDER, default='m')
    bday = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to="pics/")

    def __str__(self):
        return str(self.roll_no) + '-' + self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    teacher_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=30)
    school_id = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    bday = models.DateField()
    student_ids = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
