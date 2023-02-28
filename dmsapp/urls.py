from django.urls import path

from dmsapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('manager_reg', views.manager_reg, name='manager_reg'),
    path('principal_reg',views.principal_reg,name='principal_reg'),

    #######################MANAGER#################################
    path('manager_home', views.manager_home, name='manager_home'),
    path('student_view', views.student_view, name='student_view'),
    path('notification_view_mng', views.notification_view_mng, name='notification_view_mng'),
    path('teacher_view', views.teacher_view, name='teacher_view'),

    ########################PRINCIPAL###############################
    path('principal_home', views.principal_home, name='principal_home'),
    path('student_view_princi', views.student_view_princi, name='student_view_princi'),
    path('teacher_view_princi', views.teacher_view_princi, name='teacher_view_princi'),
    path('notification_view_princi', views.notification_view_princi, name='notification_view_princi'),
    path('view_attendance_princi', views.view_attendance_princi, name='view_attendance_princi'),
    path('day_attendance_princi/<date>',views.day_attendance_princi,name='day_attendance_princi'),
    path('result_view_princi',views.result_view_princi,name='result_view_princi'),


    ####################################Teacher##################################
    path('teacher_home', views.teacher_home, name='teacher_home'),
    path('add_att', views.add_att, name='add_att'),
    path('add_attendance_teacher',views.add_attendance_teacher,name='add_attendance_teacher'),
    path('view_attendance_teacher', views.view_attendance_teacher, name='view_attendance_teacher'),
    path('day_attendance_teacher_1/<date>',views.day_attendance_teacher_1,name='day_attendance_teacher_1'),
    path('day_attendance_teacher_2/<date>', views.day_attendance_teacher_2, name='day_attendance_teacher_2'),
    path('day_attendance_teacher_3/<date>', views.day_attendance_teacher_3, name='day_attendance_teacher_3'),
    path('day_attendance_admin_1/<date>', views.day_attendance_admin_1, name='day_attendance_admin_1'),
    path('day_attendance_admin_2/<date>', views.day_attendance_admin_2, name='day_attendance_admin_2'),
    path('day_attendance_admin_3/<date>', views.day_attendance_admin_3, name='day_attendance_admin_3'),
    path('delete_attendance_admin3/<int:id>', views.delete_attendance_admin3, name='delete_attendance_admin3'),
    path('mark_teacher/<int:id>', views.mark_teacher, name='mark_teacher'),
    path('result_add', views.result_add, name='result_add'),
    path('result_view', views.result_view, name='result_view'),
    path('result_delete/<int:id>/', views.result_delete, name='result_delete'),
    path('notification_view_teacher', views.notification_view_teacher, name='notification_view_teacher'),
    path('student_view_teacher', views.student_view_teacher, name='student_view_teacher'),
    path('add_Timetable_teacher', views.add_Timetable_teacher, name='add_Timetable_teacher'),
    path('Timetable_view_teacher',views.Timetable_view_teacher,name='Timetable_view_teacher'),
    path('Internal_add',views.Internal_add,name='Internal_add'),
    path('Internal_view',views.Internal_view,name='Internal_view'),
    path('int_middle',views.int_middle,name='int_middle'),
    path('Internal_view1',views.Internal_view1,name='Internal_view1'),
    path('Internal_view3',views.Internal_view3,name='Internal_view3'),
    path('Internal_view4',views.Internal_view4,name='Internal_view4'),
    path('Internal_view5',views.Internal_view5,name='Internal_view5'),
    path('Internal_view6',views.Internal_view6,name='Internal_view6'),
    path('del_int6/<int:id>',views.del_int6,name='del_int6'),
    path('del_int5/<int:id>', views.del_int5, name='del_int5'),
    path('del_int4/<int:id>', views.del_int4, name='del_int4'),
    path('del_int3/<int:id>', views.del_int3, name='del_int3'),
    path('del_int1/<int:id>', views.del_int1, name='del_int1'),
    path('del_int/<int:id>', views.del_int2, name='del_int'),






    ########################################Admin####################################
    path('admin_home',views.admin_home,name='admin_home'),
    path('Internal_add_admin',views.Internal_add_admin,name='Internal_add_admin'),
    path('Internal_view_admin',views.Internal_view_admin,name='Internal_view_admin'),
    path('Internal_edit/<int:id>',views.Internal_edit,name='Internal_edit'),
    path('Internal_delete/<int:id>',views.Internal_delete,name='Internal_delete'),
    path('Notification_add',views.Notification_add,name='Notification_add'),
    path('Notification_view',views.Notification_view,name='Notification_view'),
    path('Notification_edit/<int:id>',views.Notification_edit,name='Notification_edit'),
    path('Notification_delete/<int:id>',views.Notification_delete,name='Notification_delete'),
    path('Students_view_adm',views.Students_view_adm,name='Students_view_adm'),
    path('Students_edit/<int:id>',views.Students_edit,name='Students_edit'),
    path('Students_delete/<int:id>',views.Students_delete,name='Students_delete'),
    path('Teacher_view_adm',views.Teacher_view_adm,name='Teacher_view_adm'),
    path('Teachers_edit/<int:id>',views.Teachers_edit,name='Teachers_edit'),
    path('Teachers_delete/<int:id>',views.Teachers_delete,name='Teachers_delete'),
    path('add_attendance',views.add_attendance,name='add_attendance'),
    path('mark/<int:id>',views.mark,name='mark'),
    path('view_attendance',views.view_attendance,name='view_attendance'),
    path('day_attendance/<date>',views.day_attendance,name='day_attendance'),
    path('add_Timetable',views.add_Timetable,name='add_Timetable'),
    path('Timetable_view_adm',views.Timetable_view_adm,name='Timetable_view_adm'),
    path('Timetable_delete/<int:id>',views.Timetable_delete,name='Timetable_delete'),

    #########################################Student################################
    path('student_home',views.student_home,name='student_home'),
    path('Internal_view_student',views.Internal_view_student,name='Internal_view_student'),
    path('profile_view',views.profile_view,name='profile_view'),
    path('Timetable_view_stud',views.Timetable_view_stud,name='Timetable_view_stud'),
    path('Notification_view_stud',views.Notification_view_stud,name='Notification_view_stud'),
    path('view_attendance_stud',views.view_attendance_stud,name='view_attendance_stud'),
    path('result_view_stud',views.result_view_stud,name='result_view_stud'),

    path('`register_view`',views.register_view,name='register_view'),
    path('add_Timetable',views.add_Timetable,name='add_Timetable'),
    path('view',views.view,name='view'),
    path('timetable_view', views.timetable_view, name='timetable_view'),
    path('Programme',views.Programme,name='Programme'),

    path('student_reg', views.student_reg, name='student_reg'),
    path('teacher_reg', views.teacher_reg, name='teacher_reg'),
    path('view_attendance_admin', views.view_attendance_admin, name='view_attendance_admin'),




    # path('Attendance',views.Attendance,name='Attendance'),
    # path('Result',views.Result,name='Result')
]