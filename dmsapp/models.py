
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_principal = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    dob = models.DateField(null=True,blank=True)
    address = models.TextField()
    contact_no = models.CharField(max_length=50)
    email_id = models.EmailField()
    # emp_id = models.IntegerField()
    qualification = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=50)
    admission_no = models.IntegerField(null=True,blank=True)
    roll_no = models.CharField(max_length=20,null=True,blank=True)
    course = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=30)
    parent_contact = models.CharField(max_length=15)
    year_of_joining = models.DateField(null=True,blank=True)
    Designation = models.CharField(max_length=30)

    def __str__(self):
        return str(self.roll_no)

class Timetable(models.Model):
    day = models.CharField(max_length=30,null=True)
    subject1 = models.CharField(max_length=30)
    subject2 = models.CharField(max_length=30)
    subject3 = models.CharField(max_length=30)
    subject4 = models.CharField(max_length=30)
    subject5 = models.CharField(max_length=30)

class Notification(models.Model):
     subject = models.CharField(max_length=30)
     date = models.DateField()
     time = models.TimeField()
     venue = models.CharField(max_length=30)

class Attendance(models.Model):
    student = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.DateField()
    attendance = models.CharField(max_length=100)
    time = models.TimeField()

class Result(models.Model):
    semester = models.CharField(max_length=25)
    student = models.ForeignKey(Login, on_delete=models.CASCADE)
    result = models.FileField(upload_to='resultfiles')

class Internal_mark(models.Model):
    student=models.CharField(max_length=25,null=True)
    subject = models.CharField(max_length=25)
    Roll_No=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    seminar = models.IntegerField()
    assignment = models.IntegerField()
    test_paper = models.IntegerField()
    semester=models.CharField(max_length=25,null=True)
    attendance=models.IntegerField(null=True)
    total = models.IntegerField(null=True)

    def get_total_marks(self):
        return self.seminar+self.assignment+self.test_paper+self.attendance
    def __str__(self):
        return self.Roll_No

class Timetableup(models.Model):
    semester = models.CharField(max_length=25,null=True)
    files = models.FileField(upload_to='tablefiles')
    date = models.DateField(null=True)






















































































































































































































































