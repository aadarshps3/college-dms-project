import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

from dmsapp.filters import StudentFilter, SubjectFilter
from dmsapp.forms import timetableform, internal_markform,PrincipalForm, teacherform, Managerform, \
    studentform,ResultForm,ProgrammeForm
from dmsapp.models import Timetable, Login, Notification, Result, Attendance, Internal_mark, Timetableup


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("admin_home")
            elif user.is_principal:
                return redirect("principal_home")
            elif user.is_manager:
                return redirect("manager_home")
            elif user.is_teacher:
                return redirect("teacher_home")
            elif user.is_student:
                return redirect("student_home")
        else:
            messages.info(request,"user not found")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def manager_reg(request):
    form1 = Managerform()
    if request.method == "POST":
        form1 = Managerform(request.POST)
        if form1.is_valid():
            user = form1.save(commit=False)
            user.is_manager = True
            form1.save()
            messages.info(request, "student added successfully")
            return redirect('login_view')
    return render(request, "manager_reg.html", {"form1": form1})

###############################Manager#############################
def manager_home(request):
    return render(request,"manager_temp/index.html")

def student_view(request):
    data = Login.objects.filter(is_student=True)
    studentFilter = StudentFilter(request.GET, queryset=data)
    data = studentFilter.qs
    context = {
        'data': data,
        'studentFilter': studentFilter
    }
    return render(request, 'manager_temp/student_view.html',context)

def notification_view_mng(request):
    data = Notification.objects.all()
    return render(request,'manager_temp/Notification_view.html',{'data': data})

def teacher_view(request):
    data = Login.objects.filter(is_teacher=True)
    return render(request,'manager_temp/teacher_view.html',{'data':data})

def principal_reg(request):
    form=PrincipalForm()
    if request.method=="POST":
        form=PrincipalForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_principal=True
            user.save()
            messages.info(request,"principal added successfully")
            return redirect("login_view")
    return render(request,"principal_reg.html",{'form':form})

############################princiapl###########################
def principal_home(request):
    return render(request,"principal_temp/index.html")

def student_view_princi(request):
    data = Login.objects.filter(is_student=True)
    studentFilter = StudentFilter(request.GET, queryset=data)
    data = studentFilter.qs
    context = {
        'data': data,
        'studentFilter': studentFilter
    }
    return render(request, 'principal_temp/student_view.html',context)

def teacher_view_princi(request):
    data = Login.objects.filter(is_teacher=True)
    return render(request,'principal_temp/teacher_view.html',{'data':data})

def notification_view_princi(request):
    data = Notification.objects.all()
    return render(request,'principal_temp/Notification_view.html',{'data': data})

def view_attendance_princi(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'principal_temp/view_attendance.html', {'attendances': attendance})

def day_attendance_princi(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendances': attendance,
        'date': date
    }
    return render(request, 'principal_temp/day_attendance.html', context)

def result_view_princi(request):
    data = Result.objects.all()
    return render(request,'principal_temp/result_view.html',{"data":data})

############################################Teacher##########################
def teacher_home(request):
    return render(request,"teacher_temp/index.html")

def result_add(request):
    form = ResultForm()
    if request.method == "POST":
        form = ResultForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result_view')
    return render(request,'teacher_temp/result_add.html',{"form":form})

def result_view(request):
    data = Result.objects.all()
    return render(request,'teacher_temp/result_view.html',{"data":data})

def result_delete(request,id):
    data = Result.objects.get(id=id)
    data.delete()
    return redirect('result_view')

def add_att(request):
    return render(request,'teacher_temp/add_atte.html')


def add_attendance_teacher(request):
    data = Login.objects.filter(is_student=True)
    studentFilter = StudentFilter(request.GET, queryset=data)
    data = studentFilter.qs
    context = {
        'data': data,
        'studentFilter': studentFilter
    }
    return render(request, 'teacher_temp/add_attendence.html', context)

now = datetime.datetime.now()

def mark_teacher(request, id):
    user = Login.objects.get(id=id)
    att = Attendance.objects.filter(student=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's Attendance Already marked for this Student ")
        return redirect('add_attendance_teacher')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user, date=datetime.date.today(), attendance=attndc, time=now.time()).save()
            messages.info(request, "Attendance Added successfully ")
            return redirect('add_attendance_teacher')
    return render(request, 'teacher_temp/mark_attendance.html')

def view_attendance_teacher(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'teacher_temp/view_attendance.html', {'attendances': attendance})


def day_attendance_teacher_1(request, date):
    attendance = Attendance.objects.filter(date=date)

    # student_year_of_joining = "2020"
    today = datetime.date.today()
    first_year =today.year - 1




    x1 = attendance.filter(student__year_of_joining__year=first_year)


    # y = x.year()
    # print(y)
    context = {

        'attendancesx1': x1,
        'date': date
    }
    return render(request, 'teacher_temp/day_attendance1.html', context)


def day_attendance_teacher_3(request, date):
    attendance = Attendance.objects.filter(date=date)

    # student_year_of_joining = "2020"
    today = datetime.date.today()
    third_year = today.year - 3


    x3 = attendance.filter(student__year_of_joining__year=third_year)


    context = {
        'attendancesx3': x3,

        'date': date
    }
    return render(request, 'teacher_temp/day_attendance3.html', context)


def day_attendance_teacher_2(request, date):
    attendance = Attendance.objects.filter(date=date)

    # student_year_of_joining = "2020"
    today = datetime.date.today()

    second_year = today.year - 2




    x2 = attendance.filter(student__year_of_joining__year=second_year)



    # y = x.year()
    # print(y)
    context = {

        'attendancesx2': x2,

        'date': date
    }
    return render(request, 'teacher_temp/day_attendance2.html', context)

def notification_view_teacher(request):
    data = Notification.objects.all()
    return render(request,'teacher_temp/Notification_view.html',{'data': data})

def student_view_teacher(request):
    data = Login.objects.filter(is_student=True)
    studentFilter = StudentFilter(request.GET, queryset=data)
    data = studentFilter.qs
    context = {
        'data': data,
        'studentFilter': studentFilter
    }
    return render(request, 'teacher_temp/student_view.html', context)

def add_Timetable_teacher(request):
    form = timetableform()
    print(form)
    if request.method == "POST":
        form = timetableform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Timetable_view_teacher')
    return render(request,'teacher_temp/add_Timetable.html',{"form":form})

def Timetable_view_teacher(request):
    data = Timetableup.objects.all()
    return render(request,'teacher_temp/Timetable_view.html',{'data':data})

def Internal_add(request):
    form = internal_markform()
    if request.method == "POST":
        form = internal_markform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('int_middle')
    return render(request,'teacher_temp/Internal_add.html',{'form':form})

def Internal_view1(request):
    data1 = Internal_mark.objects.filter(semester="First Semester")
    subjectFilter = SubjectFilter(request.GET, queryset=data1)
    data = subjectFilter.qs
    context = {
        'data': data,
        'subjectFilter': subjectFilter
    }
    return render(request, 'teacher_temp/Internal_view1.html', context)
def del_int1(request,id):
    data=Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view1')


def Internal_view(request):
    data1 = Internal_mark.objects.filter(semester="Second Semester")
    subjectFilter = SubjectFilter(request.GET, queryset=data1)
    data = subjectFilter.qs
    context = {
        'data': data,
        'subjectFilter': subjectFilter
    }
    return render(request, 'teacher_temp/Internal_view.html', context)
def del_int2(request,id):
    data=Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view2')




def Internal_view3(request):
    data1 = Internal_mark.objects.filter(semester="Third Semester")
    subjectFilter = SubjectFilter(request.GET, queryset=data1)
    data = subjectFilter.qs
    context = {
        'data': data,
        'subjectFilter': subjectFilter
    }
    return render(request, 'teacher_temp/Internal_view3.html', context)
def del_int3(request,id):
    data=Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view3')


def Internal_view4(request):
    data1 = Internal_mark.objects.filter(semester="Fourth Semester")
    subjectFilter = SubjectFilter(request.GET, queryset=data1)
    data = subjectFilter.qs
    context = {
        'data': data,
        'subjectFilter': subjectFilter
    }
    return render(request, 'teacher_temp/Internal_view4.html', context)
def del_int4(request,id):
    data=Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view4')



def Internal_view5(request):
    data1 = Internal_mark.objects.filter(semester="Fifth Semester")

    subjectFilter = SubjectFilter(request.GET, queryset=data1)
    data = subjectFilter.qs
    context = {
        'data': data,
        'subjectFilter': subjectFilter
    }
    return render(request, 'teacher_temp/Internal_view5.html', context)
def del_int5(request,id):
    data=Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view5')



def Internal_view6(request):
    data1 = Internal_mark.objects.filter(semester="Sixth Semester")
    subjectFilter = SubjectFilter(request.GET, queryset=data1)
    data = subjectFilter.qs
    context = {
        'data': data,
        'subjectFilter': subjectFilter
    }
    return render(request,'teacher_temp/Internal_view6.html',context)
def del_int6(request,id):
    data=Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view6')

def int_middle(request):
    return render(request,'teacher_temp/int_middle.html')

##########################################Admin###########################
def admin_home(request):
    return render(request,"admin_temp/index.html")

def Internal_add_admin(request):
    form = internal_markform()
    if request.method == "POST":
        form = internal_markform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Internal_view_admin')
    return render(request,'admin_temp/Internal_add.html',{'form':form})

def Internal_view_admin(request):
    data = Internal_mark.objects.all()
    return render(request,'admin_temp/Internal_view.html',{'data':data})

def Internal_edit(request,id):
    data = Internal_mark.objects.get(id=id)
    form = internal_markform(instance=data)
    if request.method == 'POST':
        form = internal_markform(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            return redirect('Internal_view_admin')
    return render(request,'admin_temp/Internal_edit.html',{'form':form})

def Internal_delete(request,id):
    data = Internal_mark.objects.get(id=id)
    data.delete()
    return redirect('Internal_view_admin')


def Notification_add(request):
    form = ProgrammeForm()
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Notification_view')
    return render(request, 'admin_temp/Notification_add.html', {"form": form})

def Notification_view(request):
    data = Notification.objects.all()
    return render(request,'admin_temp/Notification_view.html',{"data":data})

def Notification_edit(request,id):
    data = Notification.objects.get(id=id)
    form = ProgrammeForm(instance=data)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            return redirect('Notification_view')
    return render(request,'admin_temp/Notification_edit.html',{'form':form})

def Notification_delete(request,id):
    data = Notification.objects.get(id=id)
    data.delete()
    return redirect('Notification_view')

def Students_view_adm(request):
    data = Login.objects.filter(is_student=True)
    studentFilter = StudentFilter(request.GET,queryset=data)
    data = studentFilter.qs
    context = {
        'data':data,
        'studentFilter':studentFilter
    }
    return render(request,'admin_temp/student_view.html',context)

def Students_edit(request,id):
    data = Login.objects.get(id=id)
    form = studentform(instance=data)
    if request.method == 'POST':
        form = studentform(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('Students_view_adm')
    return render(request, 'admin_temp/Students_edit.html', {'form': form})

def Students_delete(request,id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('Students_view_adm')




def Teacher_view_adm(request):
    data = Login.objects.filter(is_teacher=True)
    return render(request,'admin_temp/teacher.html',{'data':data})

def Teachers_edit(request,id):
    data = Login.objects.get(id=id)
    form = teacherform(instance=data)
    if request.method == 'POST':
        form = teacherform(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('Teacher_view_adm')
    return render(request, 'admin_temp/Teachers_edit.html', {'form': form})

def Teachers_delete(request,id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('Teacher_view_adm')

def add_attendance(request):
    data = Login.objects.filter(is_student=True)
    print(data)
    return render(request, 'admin_temp/add_attendence.html', {'data': data})

now = datetime.datetime.now()


def mark(request, id):
    user = Login.objects.get(id=id)
    att = Attendance.objects.filter(student=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's Attendance Already marked for this Student ")
        return redirect('add_attendance')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user, date=datetime.date.today(), attendance=attndc, time=now.time()).save()
            messages.info(request, "Attendance Added successfully ")
            return redirect('add_attendance')
    return render(request, 'admin_temp/mark_attendance.html')

def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'admin_temp/view_attendance.html', {'attendances': attendance})

def day_attendance(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendances': attendance,
        'date': date
    }
    return render(request, 'admin_temp/day_attendance.html', context)

def add_Timetable(request):
    form = timetableform()
    print(form)
    if request.method == "POST":
        form = timetableform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Timetable_view_adm')
    return render(request,'admin_temp/add_Timetable.html',{"form":form})

def Timetable_view_adm(request):
    data = Timetableup.objects.all()
    return render(request,'admin_temp/Timetable_view.html',{'data':data})



def Timetable_delete(request,id):
    data = Timetableup.objects.get(id=id)
    data.delete()
    return redirect('Timetable_view_adm')

######################################Student#####################################
def student_home(request):
    return render(request,"student_temp/index.html")

def Internal_view_student(request):
    u = request.user
    print(u)
    data = Internal_mark.objects.filter(Roll_No=u)
    return render(request,'student_temp/Internal_view.html',{'data':data})

def profile_view(request):
    u = request.user.username
    print(u)
    print("hi")
    data = Login.objects.filter(username=u)
    print(data)
    return render(request,'student_temp/profile_view.html',{'data':data})

def Notification_view_stud(request):
    data = Notification.objects.all()
    return render(request,'student_temp/Notification_view.html',{"data":data})

def Timetable_view_stud(request):
    data = Timetableup.objects.all()
    return render(request,'student_temp/Timetable_view.html',{'data':data})

def view_attendance_stud(request):
    u=request.user
    # u = Login.objects.get(username=u)
    attendance = Attendance.objects.filter(student=u)
    return render(request, 'student_temp/view_attendance.html', {'attendances': attendance})

def result_view_stud(request):
    u=request.user
    data = Result.objects.filter(student=u)
    return render(request,'student_temp/result_view.html',{"data":data})

def register_view(request):
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')






def student(request):
    return render(request,"student/student.html")



#
#
#
#
#










def student_reg(request):
     form1=studentform()
     if request.method == "POST":
         form1=studentform(request.POST)
         if form1.is_valid():
             user=form1.save(commit=False)
             user.is_student=True
             user.save()
             messages.info(request,"student added successfully")
             return redirect('login_view')
     return render(request,"student_reg.html",{"form1":form1})





def teacher_reg(request):
     form1=teacherform()
     if request.method == "POST":
         form1=teacherform(request.POST)
         if form1.is_valid():
          user=form1.save(commit=False)
          user.is_teacher=True
          user.save()
          messages.info(request, "teacher added successfully")
          return redirect('login_view')
     return render(request,"teacher_reg.html",{"form1":form1})



def timetable_view(request):
    data=Timetable.objects.all()
    return render(request,"view.html",{"data":data})

def view(request):
    data=Internal_Mark.objects.all()
    return render(request,"view.html",{"data":data})


def Programme(request):
    form = programmeform()
    print(form)
    if request.method == "POST":
        form = programmeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'programme.html',{"form":form})


# def add_Attendance(request, student):
#     student = student.objects.filter(approvel_status=True)
#     return render(request,'adminpages/student_list.html',{'student:student'})
#
# now = datetime.datetime.now()
#
# def view_Attendance(request)
#     value_list = Attendance.objects.value.list('date',flat=True).distinct()
#     attendence = {}
#     for value in value_list:
#          attendence[value] = attendence.objects.filter(date=value)
#         return render(request, 'adminpages/view_attendence.html', {'attendances':Attendance})
#
#
# def day_attendance(request,date):
#     attendance = Attendance.objects.filter(date=date)
#     context = {
#     'attendances':attendance,
#     'date': date
#     }
#     return render(request,'adminpages/day_attendance.html', context)
#
#
#
#

def view_attendance_admin(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'admin_temp/view_attendance1.html', {'attendances': attendance})


def day_attendance_admin_1(request, date):
    attendance = Attendance.objects.filter(date=date)

    # student_year_of_joining = "2020"
    today = datetime.date.today()
    first_year =today.year - 1




    x1 = attendance.filter(student__year_of_joining__year=first_year)


    # y = x.year()
    # print(y)
    context = {

        'attendancesx1': x1,
        'date': date
    }
    return render(request, 'admin_temp/day_attendance1.html', context)


def day_attendance_admin_3(request, date):
    attendance = Attendance.objects.filter(date=date)

    # student_year_of_joining = "2020"
    today = datetime.date.today()
    third_year = today.year - 3


    x3 = attendance.filter(student__year_of_joining__year=third_year)


    context = {
        'attendancesx3': x3,

        'date': date
    }
    return render(request, 'admin_temp/day_attendance3.html', context)

def delete_attendance_admin3(request,id):
    data = Attendance.objects.get(id=id)
    data.delete()
    return redirect('view_attendance_admin')


def day_attendance_admin_2(request, date):
    attendance = Attendance.objects.filter(date=date)

    # student_year_of_joining = "2020"
    today = datetime.date.today()

    second_year = today.year - 2




    x2 = attendance.filter(student__year_of_joining__year=second_year)



    # y = x.year()
    # print(y)
    context = {

        'attendancesx2': x2,

        'date': date
    }
    return render(request, 'admin_temp/day_attendance2.html', context)



