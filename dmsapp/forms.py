from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import manager

from dmsapp.models import Login, Timetable, Notification, Result, Internal_mark, Timetableup


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'
# PRINCIPAL REGISTER

gender_choices=(
    ('male','male'),
    ('female','female'),
    ('other','other'),
)
class PrincipalForm(UserCreationForm):
    dob=forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(choices=gender_choices)
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)

    class Meta:
        model = Login
        fields = ('username','password1','password2','name','email','contact_no','gender','dob','address','qualification')


# manager register

class Managerform(UserCreationForm):
     dob = forms.DateField(widget=DateInput)
     gender = forms.ChoiceField(choices=gender_choices)
     password1 = forms.CharField(label='password', widget=forms.PasswordInput, )
     password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput, )

     class Meta:
         model = Login
         fields =('username','password1','password2','name','email','contact_no','gender','dob','address','qualification')


# teacher register

class teacherform(UserCreationForm):
     dob = forms.DateField(widget=DateInput)
     gender=forms.ChoiceField(choices=gender_choices)
     password1 = forms.CharField(label='Password',widget=forms.PasswordInput, )
     password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput, )

     class Meta:
         model = Login
         fields =('username','password1','password2','name','email','contact_no','gender','dob','address','qualification','Designation')


 # student register
course_choice = (
    ('BSC Physics', 'BSC Physics'),
    ('BSC Maths', 'BSC Maths'),
    ('BSC ComputerScience', 'BSC ComputerScience'),
    ('BCA', 'BCA'),
    ('BSC Chemistry', 'BSC Chemistry'),
    ('BA English', 'BA English'),
    ('BA Malayalam', 'BA Malayalam'),
    ('BBA ', 'BBA'),
)

class studentform(UserCreationForm):
    dob = forms.DateField(widget=DateInput)
    year_of_joining = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(choices=gender_choices)
    course = forms.ChoiceField(choices=course_choice)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput, )

    class Meta:
         model = Login
         fields =('username','password1','password2','name','email','contact_no','gender','dob','address','admission_no','roll_no','blood_group','course','year_of_joining','parent_name','parent_contact')


sem_choice = (
    ('First Semester','First Semester'),
    ('Second Semester','Second Semester'),
    ('Third Semester','Third Semester'),
    ('Fourth Semester','Fourth Semester'),
    ('Fifth Semester','Fifth Semester'),
    ('Sixth Semester','Sixth Semester')
)
class timetableform(forms.ModelForm):
    semester = forms.ChoiceField(choices=sem_choice)
    class Meta:
        model = Timetableup
        fields=('semester','files')



class internal_markform(forms.ModelForm):
    semester = forms.ChoiceField(choices=sem_choice)
    class Meta:
        model = Internal_mark
        fields=('student','semester','Roll_No','subject','seminar','assignment','test_paper','attendance')



class ProgrammeForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput, )
    class Meta:
        model = Notification
        fields=('subject','date','time','venue')

semester_choice = (
    ('First Semester', 'First Semester'),
    ('Second Semester', 'Second Semester'),
    ('Third Semester', 'Third Semester'),
    ('Fourth Semester', 'Fourth Semester'),
    ('Fifth Semester', 'Fifth Semester'),
    ('Sixth Semester', 'Sixth Semester'),
)

class ResultForm(forms.ModelForm):
    semester = forms.ChoiceField(choices=semester_choice)
    class Meta:
        model = Result
        fields=('semester','student','result')

