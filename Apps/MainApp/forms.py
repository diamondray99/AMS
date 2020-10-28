# All imports-----------------------------------------------------------------------------------------------------------

# Django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# Project imports
from Apps.MainApp.models import *

# Third Party imports
from dobwidget import DateOfBirthWidget


# All Forms------------------------------------------------------------------------------------------------------------


# College Details Form
class CollegeDetailForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = CollegeDetailModel
        fields = [
            'title',
            'sub_title',
            'details',
            'image',
            'file',
            'active',
        ]


# Course Form
class CoursesForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = CourseModel
        fields = [
            'course',
            'image',
            'eligibility',
            'duration_of_course',
            'syllabus',
            'extra_details',
            'year_1_fees',
            'year_2_fees',
            'year_3_fees',
            'active',
        ]


# Cutoff Form
class StudentCapacityForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentCapacityModel
        fields = [
            'course',
            'year_1',
            'year_2',
            'year_3',
            'student_capacity',
            'active',
        ]


# Student Admission Form
class FyStudentForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = [
            'uid',
            'year_2',
            'year_3',
            'semester_1_SGPI',
            'semester_2_SGPI',
            'semester_3_SGPI',
            'semester_4_SGPI',
            'previous_year_mark_sheet',
            'aggregate_1',
            'aggregate_2',
            'transaction_id',
            'payment_date',
            'sent_p_mail',
            'in_house',
            'out_house',
            'slug',
            'verified',
            'sent_v_mail',
            'selected',
            'sent_s_mail',
            'fees_paid',
            'sent_a_mail',
            'username',
            'password',
            'admitted',
            'created_at',
            'updated_at',
        ]
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }


class SyInStudentForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = [
            'uid',
            'year_1',
            'year_3',
            'leaving_certificate',
            'previous_college_name',
            'HSC_mark_sheet',
            'HSC_percentage',
            'SSC_mark_sheet',
            'SSC_percentage',
            'semester_3_SGPI',
            'semester_4_SGPI',
            'MU_application',
            'MU_application_no',
            'aggregate_1',
            'aggregate_2',
            'transaction_id',
            'payment_date',
            'sent_p_mail',
            'out_house',
            'slug',
            'verified',
            'sent_v_mail',
            'selected',
            'sent_s_mail',
            'fees_paid',
            'sent_a_mail',
            'username',
            'password',
            'admitted',
            'created_at',
            'updated_at',
        ]
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }


class SyOutStudentForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = [
            'uid',
            'year_1',
            'year_3',
            'HSC_mark_sheet',
            'HSC_percentage',
            'SSC_mark_sheet',
            'SSC_percentage',
            'semester_3_SGPI',
            'semester_4_SGPI',
            'MU_application',
            'MU_application_no',
            'aggregate_1',
            'aggregate_2',
            'transaction_id',
            'payment_date',
            'sent_p_mail',
            'in_house',
            'slug',
            'verified',
            'sent_v_mail',
            'selected',
            'sent_s_mail',
            'fees_paid',
            'sent_a_mail',
            'username',
            'password',
            'admitted',
            'created_at',
            'updated_at',
        ]
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }


class TyInStudentForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = [
            'uid',
            'year_1',
            'year_2',
            'leaving_certificate',
            'previous_college_name',
            'HSC_mark_sheet',
            'HSC_percentage',
            'SSC_mark_sheet',
            'SSC_percentage',
            'MU_application',
            'MU_application_no',
            'aggregate_1',
            'aggregate_2',
            'transaction_id',
            'payment_date',
            'sent_p_mail',
            'out_house',
            'slug',
            'verified',
            'sent_v_mail',
            'selected',
            'sent_s_mail',
            'fees_paid',
            'sent_a_mail',
            'username',
            'password',
            'admitted',
            'created_at',
            'updated_at',
        ]
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }


class TyOutStudentForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = [
            'uid',
            'year_1',
            'year_2',
            'HSC_mark_sheet',
            'HSC_percentage',
            'SSC_mark_sheet',
            'SSC_percentage',
            'MU_application',
            'MU_application_no',
            'aggregate_1',
            'aggregate_2',
            'transaction_id',
            'payment_date',
            'sent_p_mail',
            'in_house',
            'slug',
            'verified',
            'sent_v_mail',
            'selected',
            'sent_s_mail',
            'fees_paid',
            'sent_a_mail',
            'username',
            'password',
            'admitted',
            'created_at',
            'updated_at',
        ]
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }


# Student Verification Form
class VerifyForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = [
            'verified',
        ]


# Student Selection Form
class SelectForm(forms.Form):  # Tested and PWNE
    agreement = forms.BooleanField(required=True, label='I accept all.')


# Payment Verification Form
class PaymentVerify(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = [
            'fees_paid',
        ]


# Payment Verification Form
class PaymentLinkForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = [
            'transaction_id',
            'payment_date',
        ]


# Registration Form
class AdmitForm(ModelForm):  # Tested and PWNE
    class Meta:
        model = StudentModel
        fields = [
            'admitted',
        ]


# WorkForce Registration Form
class WorkForceRegistrationForm(UserCreationForm):   # Tested and PWNE
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'is_staff',
            'is_superuser',
        ]


class WorkForceUpdateForm(ModelForm):   # Tested and PWNE
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]
