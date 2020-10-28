from django.urls import path
from .views import *

urlpatterns = [

    path('dashboard/', dashboard.as_view(), name='dashboard'),
    path('', home.as_view(), name='home'),
    path('about/', about.as_view(), name='about'),

    # College Details # Tested and PWNE
    path('list_college_details/', list_college_details.as_view(), name='list_college_details'),
    path('detail_college_details/<slug:slug>', detail_college_details.as_view(), name='detail_college_details'),
    path('create_college_details/', create_college_details.as_view(), name='create_college_details'),
    path('update_college_details/<slug:slug>/', update_college_details.as_view(), name='update_college_details'),
    path('<slug:slug>/delete_college_details/', delete_college_details.as_view(), name='delete_college_details'),

    # Course # Tested and PWNE
    path('course_list/', course_list.as_view(), name='course_list'),
    path('course_detail/<slug:slug>/', course_detail.as_view(), name='course_detail'),
    path('create_course/', create_course.as_view(), name='create_course'),
    path('update_course/<slug:slug>/', update_course.as_view(), name='update_course'),
    path('<slug:slug>/delete_course/', delete_course.as_view(), name='delete_course'),

    # Student Capacity # Tested and PWNE
    path('student_capacity_list/', student_capacity_list.as_view(), name='student_capacity_list'),
    path('create_student_capacity/', create_student_capacity.as_view(), name='create_student_capacity'),
    path('update_student_capacity/<slug:slug>/', update_student_capacity.as_view(), name='update_student_capacity'),
    path('<slug:slug>/delete_student_capacity/', delete_student_capacity.as_view(), name='delete_student_capacity'),

    # Admission Forms and routes # Tested and PWNE
    path('sy-in-out-house/', SyInOutHouse.as_view(), name='sy_in_out_house'),  
    path('ty-in-out-house/', TyInOutHouse.as_view(), name='ty_in_out_house'),  
    path('choose-year/', ChooseYear.as_view(), name='choose_year'),  
    path('fy-form', FyStudent.as_view(), name='fy_form'),  
    path('sy-in-form', SyInStudent.as_view(), name='sy_in_form'),  
    path('sy-out-form', SyOutStudent.as_view(), name='sy_out_form'),  
    path('ty-in-form', TyInStudent.as_view(), name='ty_in_form'),  
    path('ty-out-form', TyOutStudent.as_view(), name='ty_out_form'),  

    # Student Views # Tested and PWNE
    path('view/', ViewStudents.as_view(), name='view_students'),

    # Student URD
    path('detail/<slug:slug>', student_details.as_view(), name='student_details'),
    path('student-update/<slug:slug>/', FyStudent_update.as_view(), name='year_1_update'),
    path('student-update/<slug:slug>/', SyInStudent_update.as_view(), name='year_2_in_update'),
    path('student-update/<slug:slug>/', SyOutStudent_update.as_view(), name='year_2_out_update'),
    path('student-update/<slug:slug>/', TyInStudent_update.as_view(), name='year_3_in_update'),
    path('student-update/<slug:slug>/', TyOutStudent_update.as_view(), name='year_3_out_update'),
    path('student-delete/<slug:slug>/', student_delete.as_view(), name='student_delete'),

    # Student Verification # Tested and PWNE
    path('view/verify-students/', CourseForVerify.as_view(), name='courses_for_verify'),  
    path('view/verify-students/<slug:slug>/', verify_students, name='verify_students'),  
    path('view/verify-student-details/<slug:slug>/', verify_std_details,
         name='verify_std_details'),  

    # Student Selection # Tested and PWNE
    path('view/select-students/', CoursesForSelect.as_view(), name='courses_for_select'),  
    path('view/select-students/<slug:slug>/year-1/', select_year_1, name='select_year_1'),  
    path('view/select-students/<slug:slug>/year-2/', select_year_2, name='select_year_2'),  
    path('view/select-students/<slug:slug>/year-3/', select_year_3, name='select_year_3'),  


    # Student Cutoffs # Tested and PWNE
    path('cutoffs/', CoursesForCutoffs.as_view(), name='courses_for_cutoffs'),  
    path('cutoffs/<slug:slug>/', cutoffs, name='cutoffs'),  

    # Student Payment # Tested and PWNE
    path('payment/<slug:slug>/', payment_link, name='payment_link'),
    path('view/verify-payments/', CoursesForPaymentVerify.as_view(),
         name='courses_for_verify_payment'),  
    path('view/verify-payments/<slug:slug>/', verify_payment, name='verify_payment'),  
    path('view/verify-payments-deatils/<slug:slug>/', verify_payment_details,
         name='verify_payment_details'),  
    path('payment-success/', payment_success.as_view(), name='payment_success'),  


    # Student Registration # Tested and PWNE
    path('view/admit-students/', CoursesForAdmit.as_view(), name='courses_for_admit'),  
    path('view/admit-students/<slug:slug>/year-1/', admit_year_1, name='admit_year_1'),  
    path('view/admit-students/<slug:slug>/year-2/', admit_year_2, name='admit_year_2'),  
    path('view/dmi-students/<slug:slug>/year-3/', admit_year_3, name='admit_year_3'),  

    # Student Applications # Tested and PWNE
    path('student-applications/', CoursesForStudentApplication.as_view(), name='courses_for_applications'),
    path('student-applications/<slug:slug>', student_applications, name='student_applications'),

    # Verified Students # Tested and PWNE
    path('verified-students/', CoursesForVerifiedStudent.as_view(), name='courses_for_verified'),
    path('verified-students/<slug:slug>', verified_students, name='verified_students'),

    # Fees Paid Students # Tested and PWNE
    path('fees-paid-students/', CoursesForFeesPaidStudent.as_view(), name='courses_for_fees_paid'),
    path('fees-paid-students/<slug:slug>', students_Fees_paid, name='students_Fees_paid'),

    # Registered Students # Tested and PWNE
    path('student-applications/', CoursesForAdmittedStudents.as_view(), name='courses_for_admitted'),
    path('student-applications/<slug:slug>', admitted_students, name='admitted_students'),

    # Workforce # Tested and PWNE
    path('create-workforce/', create_workforce.as_view(), name='create_workforce'),
    path('update-workforce/<int:pk>/', update_workforce.as_view(), name='update_workforce'),
    path('<int:pk>/delete-workforce/', delete_workforce.as_view(), name='delete_workforce'),
    path('workforce-list/', workforce_list.as_view(), name='workforce_list'),
    path('workforce-details/<int:pk>/', workforce_detail.as_view(), name='workforce_detail'),


    # Auth Change Password # Tested and PWNE
    path('change_password/', change_password, name='change_password'),

]
