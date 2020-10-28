# Django imports
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Python Imports
from PIL import Image

# Project imports
from .forms import *


# Create your views here.

class dashboard(LoginRequiredMixin, TemplateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    template_name = 'dashboard/adminDashboard.html'


class home(ListView):  # Tested and PWNE
    model = CollegeDetailModel
    queryset = CollegeDetailModel.objects.all().filter(active=True)
    template_name = 'CRUD-temps/home-&-about/home.html'

    def get_context_data(self, *, object_list=CollegeDetailModel.objects.all(), **kwargs):
        if len(object_list) >= 1:
            for i in object_list:
                if i.image:
                    pic = '.' + i.image.url
                    image = Image.open(pic)
                    if image.size != (512, 512):
                        new_size = (512, 512)
                        new = image.resize(new_size)
                        new.save(pic)
                else:
                    pass
        else:
            pass
        return super(home, self).get_context_data()


class about(TemplateView):
    template_name = 'CRUD-temps/home-&-about/about.html'


# College Details CRUD--------------------------------------------------------------------------------------------------
class list_college_details(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CollegeDetailModel
    template_name = 'CRUD-temps/college-CRUD/retrieve/list_view.html'

    def get_context_data(self, *, object_list=CollegeDetailModel.objects.all(), **kwargs):
        if len(object_list) > 0:
            for i in object_list:
                if i.image:
                    pic = '.' + i.image.url
                    image = Image.open(pic)
                    if image.size != (512, 512):
                        new_size = (512, 512)
                        new = image.resize(new_size)
                        new.save(pic)
                else:
                    pass
        else:
            pass
        return super(list_college_details, self).get_context_data()


class detail_college_details(LoginRequiredMixin, DetailView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CollegeDetailModel
    template_name = 'CRUD-temps/college-CRUD/retrieve/detail_view.html'

    def get_context_data(self, *, object_list=CollegeDetailModel.objects.all(), **kwargs):
        for i in object_list:
            if i.image:
                pic = '.' + i.image.url
                image = Image.open(pic)
                if image.size != (512, 512):
                    new_size = (512, 512)
                    new = image.resize(new_size)
                    new.save(pic)
            else:
                pass
        return super(detail_college_details, self).get_context_data()


class create_college_details(LoginRequiredMixin, CreateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    form_class = CollegeDetailForm
    extra_context = {
        'var': 'Add',
        'title': 'Add College Details'
    }
    success_url = reverse_lazy('create_college_details')
    template_name = 'CRUD-temps/college-CRUD/create.html'


class update_college_details(LoginRequiredMixin, UpdateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CollegeDetailModel
    form_class = CollegeDetailForm
    extra_context = {
        'title': 'Update College Details',
        'var': 'Update',
    }
    template_name = 'CRUD-temps/college-CRUD/update.html'
    success_url = reverse_lazy('list_college_details')


class delete_college_details(LoginRequiredMixin, DeleteView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CollegeDetailModel
    extra_context = {
        'title': 'Delete College Details',
        'var': 'Delete',
    }
    template_name = 'CRUD-temps/college-CRUD/delete.html'
    success_url = reverse_lazy('list_college_details')


# Courses CRUD----------------------------------------------------------------------------------------------------------

class course_list(ListView):  # Tested and PWNE
    def get_context_data(self, *, object_list=CourseModel.objects.all(), **kwargs):
        if len(object_list) > 0:
            for i in object_list:
                if i.image:
                    pic = '.' + i.image.url
                    image = Image.open(pic)
                    if image.size != (512, 512):
                        new_size = (512, 512)
                        new = image.resize(new_size)
                        new.save(pic)
                else:
                    pass
        else:
            pass
        return super(course_list, self).get_context_data()

    model = CourseModel
    template_name = 'CRUD-temps/course-CRUD/retrieve/list_view.html'


class course_detail(DetailView):  # Tested and PWNE
    model = CourseModel
    template_name = 'CRUD-temps/course-CRUD/retrieve/detail_view.html'

    def get_context_data(self, *, object_list=CourseModel.objects.all(), **kwargs):
        for i in object_list:
            if i.image:
                pic = '.' + i.image.url
                image = Image.open(pic)
                if image.size != (512, 512):
                    new_size = (512, 512)
                    new = image.resize(new_size)
                    new.save(pic)
            else:
                pass
        return super(course_detail, self).get_context_data()


class create_course(LoginRequiredMixin, CreateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    form_class = CoursesForm
    extra_context = {
        'var': 'Add',
        'title': 'Add Course'
    }
    template_name = 'CRUD-temps/course-CRUD/create.html'
    success_url = reverse_lazy('create_course')


class update_course(LoginRequiredMixin, UpdateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    form_class = CoursesForm
    extra_context = {
        'title': 'Update Course',
        'var': 'Update',
    }
    template_name = 'CRUD-temps/course-CRUD/update.html'
    success_url = reverse_lazy('course_list')


class delete_course(LoginRequiredMixin, DeleteView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    extra_context = {
        'title': 'Delete Course',
        'var': 'Delete',
    }
    template_name = 'CRUD-temps/course-CRUD/delete.html'
    success_url = reverse_lazy('course_list')


# Student Capacity CRUD-----------------------------------------------------------------------------------------------

class create_student_capacity(LoginRequiredMixin, CreateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    form_class = StudentCapacityForm
    model = StudentCapacityModel
    extra_context = {
        'var': 'Submit',
        'title': 'Add Student Capacity',
        'validate': 'validate',
    }
    template_name = 'CRUD-temps/student_capacity-CRUD/create.html'
    success_url = reverse_lazy('create_student_capacity')


class student_capacity_list(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = StudentCapacityModel
    template_name = 'CRUD-temps/student_capacity-CRUD/retrieve/list_view.html'

    def get_context_data(self, *, object_list=StudentCapacityModel.objects.all(), **kwargs):
        for i in object_list:
            if i.slug:
                if object_list.filter(slug=i.slug).count() > 1:
                    i.delete()
            else:
                pass
        return super(student_capacity_list, self).get_context_data()


class update_student_capacity(LoginRequiredMixin, UpdateView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = StudentCapacityModel
    fields = [
        'course',
        'year_1',
        'year_2',
        'year_3',
        'student_capacity',
        'active',
    ]
    extra_context = {
        'title': 'Update Student Capacity',
        'var': 'Update',
    }
    template_name = 'CRUD-temps/student_capacity-CRUD/update.html'
    success_url = reverse_lazy('student_capacity_list')


class delete_student_capacity(LoginRequiredMixin, DeleteView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = StudentCapacityModel
    template_name = 'CRUD-temps/student_capacity-CRUD/delete.html'
    extra_context = {
        'title': 'Delete Cutoffs',
        'var': 'Delete',
    }
    success_url = reverse_lazy('student_capacity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context


# Student CRUD----------------------------------------------------------------------------------------------------------
class ViewStudents(TemplateView):  # Tested and PWNE
    template_name = 'dashboard/ViewStudents.html'


class ChooseYear(TemplateView):  # Tested and PWNE
    template_name = 'CRUD-temps/student-CRUD/create/choose_year.html'


class SyInOutHouse(TemplateView):  # Tested and PWNE
    template_name = 'CRUD-temps/student-CRUD/create/sy_in_out_house.html'


class TyInOutHouse(TemplateView):  # Tested and PWNE
    template_name = 'CRUD-temps/student-CRUD/create/ty_in_out_house.html'


class FyStudent(CreateView):  # Tested and PWNE
    model = StudentModel
    form_class = FyStudentForm
    template_name = 'CRUD-temps/student-CRUD/create/create_fy.html'
    success_url = reverse_lazy('fy_form')
    extra_context = {
        'var': 'Submit',
        'title': 'Admission Form',
        'validate': 'validate',
    }


class FyStudent_update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = StudentModel
    form_class = FyStudentForm
    template_name = 'CRUD-temps/student-CRUD/update/update.html'
    extra_context = {
        'var': 'Update',
        'title': 'Update Student Details',
    }
    success_url = reverse_lazy('view_students')


class SyInStudent(CreateView):  # Tested and PWNE
    model = StudentModel
    form_class = SyInStudentForm
    template_name = 'CRUD-temps/student-CRUD/create/create_in_sy.html'
    success_url = reverse_lazy('sy_in_form')
    extra_context = {
        'var': 'Submit',
        'title': 'Admission Form',
        'validate': 'validate',
    }


class SyInStudent_update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = StudentModel
    form_class = SyInStudentForm
    template_name = 'CRUD-temps/student-CRUD/update/update.html'
    success_url = reverse_lazy('view_students')


class SyOutStudent(CreateView):  # Tested and PWNE
    model = StudentModel
    form_class = SyOutStudentForm
    template_name = 'CRUD-temps/student-CRUD/create/create_out_sy.html'
    success_url = reverse_lazy('sy_out_form')
    extra_context = {
        'var': 'Submit',
        'title': 'Admission Form',
        'validate': 'validate',
    }


class SyOutStudent_update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = StudentModel
    form_class = SyOutStudentForm
    template_name = 'CRUD-temps/student-CRUD/update/update.html'
    success_url = reverse_lazy('view_students')


class TyInStudent(CreateView):  # Tested and PWNE
    model = StudentModel
    form_class = TyInStudentForm
    template_name = 'CRUD-temps/student-CRUD/create/create_in_ty.html'
    success_url = reverse_lazy('ty_in_form')
    extra_context = {
        'var': 'Submit',
        'title': 'Admission Form',
        'validate': 'validate',
    }


class TyInStudent_update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = StudentModel
    form_class = TyInStudentForm
    template_name = 'CRUD-temps/student-CRUD/update/update.html'
    success_url = reverse_lazy('view_students')


class TyOutStudent(CreateView):  # Tested and PWNE
    model = StudentModel
    form_class = TyOutStudentForm
    template_name = 'CRUD-temps/student-CRUD/create/create_out_ty.html'
    success_url = reverse_lazy('ty_out_form')
    extra_context = {
        'var': 'Submit',
        'title': 'Admission Form',
        'validate': 'validate',
    }


class TyOutStudent_update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = StudentModel
    form_class = TyOutStudentForm
    template_name = 'CRUD-temps/student-CRUD/update/update.html'
    success_url = reverse_lazy('view_students')


class student_details(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = StudentModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/detail_view.html'


class student_delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = StudentModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/detail_view.html'
    success_url = reverse_lazy('view_students')


class CourseForVerify(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/imp_operations/verification/course_for_verify.html'


@login_required(login_url=reverse_lazy('login'))
def verify_students(request, slug):  # Tested and PWNE
    year_1 = StudentModel.objects.filter(course__slug=slug, year_1=True, verified=False, admitted=False, selected=False)
    year_2 = StudentModel.objects.filter(course__slug=slug, year_2=True, verified=False, admitted=False, selected=False)
    year_3 = StudentModel.objects.filter(course__slug=slug, year_3=True, verified=False, admitted=False, selected=False)

    context = {
        'year1': year_1,
        'year2': year_2,
        'year3': year_3,
        'title': 'Verified Students',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/verification/stdVerify.html',
                  context=context)


@login_required(login_url=reverse_lazy('login'))
def verify_std_details(request, slug):  # Tested and PWNE
    form = VerifyForm(request.POST or request.GET or None)
    model = StudentModel.objects.all().filter(verified=False, sent_v_mail=False, selected=False, sent_s_mail=False,
                                              admitted=False, fees_paid=False, slug=slug)
    if request.method == 'POST':
        if form.is_valid():
            for i in model:
                if not i.verified:
                    i.verified = True
                    i.save()
                if not i.sent_v_mail:
                    send_mail(
                        subject='Verification Response Mail',
                        message='Congratulations, your application for admission has been verified by our college'
                                ' authorities and sent for the selection process.\n'
                                ' If you get selected you will receive a mail from the college authorities with the '
                                'payment link.\n So, stay tune...',
                        from_email='kirra000deathnote@gmail.com',
                        recipient_list=[i.email, ],
                        fail_silently=False,
                    )
                    i.sent_v_mail = True
                    i.save()
            return redirect('verify_students', slug)
        else:
            pass
    context = {
        'object': model,
        'form': form,
        'var': 'Submit',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/verification/verify_std_details.html',
                  context=context)


class CoursesForSelect(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/imp_operations/selection/course_for_select.html'


@login_required(login_url=reverse_lazy('login'))
def select_year_1(request, slug):
    if StudentCapacityModel.objects.all().filter(course__slug=slug, year_1=True).exists():
        model = StudentModel.objects.all().filter(verified=True, sent_v_mail=True, selected=False,
                                                  sent_s_mail=False, admitted=False, course__slug=slug,
                                                  fees_paid=False, year_1=True).order_by('-HSC_percentage')
        form = SelectForm(request.POST or request.GET or None)
        print(StudentCapacityModel.objects.get(course__slug=slug, year_1=True).student_capacity)
        if request.method == 'POST':
            if form.is_valid():
                if StudentCapacityModel.objects.get(course__slug=slug, year_1=True).student_capacity:
                    c_model = StudentCapacityModel.objects.get(course__slug=slug, year_1=True).student_capacity
                    capacity = c_model
                    print('capacity = ', capacity)

                    temp = []

                    for i in model:
                        temp.append(i)
                    print('temp : ', temp)

                    final = []
                    if len(temp) > 0:
                        for i in temp:
                            if len(final) <= int(capacity):
                                final.append(i)
                                i.selected = True
                                i.save()
                                send_mail(
                                    subject='Selection Response Mail',
                                    message='Congratulations your application for admission has been selected by our '
                                            'college authorities \n'
                                            'Here is your cutoff list link where you can check and confirm it.'
                                            'http://127.0.0.1:8000/cutoffs/ \n'
                                            'Here is your payment link from where you can pay fees and can confirm '
                                            'your admission seat in college. http://127.0.0.1:8000/payment/'
                                            + i.slug + '/ \n After the fees payment you will receive a mail of '
                                                       'payment verification.',
                                    from_email='kirra000deathnote@gmail.com',
                                    recipient_list=[i.email, ],
                                    fail_silently=False,
                                )
                                i.sent_s_mail = True
                                i.save()
                    print('final : ', final)
                    print('done!')
                    return redirect('select_year_1', slug)
                else:
                    pass
            else:
                pass

        context = {
            'object_list': model,
            'form': form,
            'var': 'Select',
        }
    else:
        return HttpResponse('Student capacity of this course for year 1 has not been created.'
                            ' Please create the student capacity of this course using dashboard.')

    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/selection/select_year_1.html',
                  context=context)


@login_required(login_url=reverse_lazy('login'))
def select_year_2(request, slug):
    if StudentCapacityModel.objects.all().filter(course__slug=slug, year_2=True).exists():
        model = StudentModel.objects.all().filter(verified=True, sent_v_mail=True, selected=False,
                                                  sent_s_mail=False, admitted=False, course__slug=slug,
                                                  fees_paid=False, year_2=True).order_by('-aggregate_1')

        form = SelectForm(request.POST or request.GET or None)
        if request.method == 'POST':
            if form.is_valid():
                if StudentCapacityModel.objects.filter(course__slug=slug, year_2=True).exists():
                    c_model = StudentCapacityModel.objects.get(course__slug=slug, year_2=True).student_capacity
                    capacity = c_model
                    print('capacity = ', capacity)
                    temp = []

                    for i in model:
                        temp.append(i)
                    print('temp : ', temp)

                    final = []
                    if len(temp) > 0:
                        for i in temp:
                            if len(final) <= int(capacity):
                                final.append(i)
                                i.selected = True
                                i.save()
                                send_mail(
                                    subject='Selection Response Mail',
                                    message='Congratulations your application for admission has been selected by our '
                                            'college authorities \n'
                                            'Here is your cutoff list link where you can check and confirm it. \n'
                                            'Here is your payment link from where you can pay fees and can confirm '
                                            'your admission seat in college.\n'
                                            'After the fees payment you will receive a mail of payment verification.',
                                    from_email='kirra000deathnote@gmail.com',
                                    recipient_list=[i.email, ],
                                    fail_silently=False,
                                )
                                i.sent_s_mail = True
                                i.save()
                    print('final : ', final)
                    print('done!')
                    return redirect('select_year_2', slug)
                else:
                    return redirect('select_year_2', slug)
            else:
                pass

        context = {
            'object_list': model,
            'form': form,
            'var': 'Select',
        }
    else:
        return HttpResponse('Student capacity of this course for year 2 has not been created.'
                            ' Please create the student capacity of this course using dashboard.')

    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/selection/select_year_2.html',
                  context=context)


@login_required(login_url=reverse_lazy('login'))
def select_year_3(request, slug):
    if StudentCapacityModel.objects.all().filter(course__slug=slug, year_3=True).exists():
        model = StudentModel.objects.all().filter(verified=True, sent_v_mail=True, selected=False,
                                                  sent_s_mail=False, admitted=False, course__slug=slug,
                                                  fees_paid=False, year_3=True).order_by('-aggregate_2')

        form = SelectForm(request.POST or request.GET or None)

        if request.method == 'POST':
            if form.is_valid():
                if StudentCapacityModel.objects.filter(course__slug=slug, year_3=True).exists():
                    c_model = StudentCapacityModel.objects.get(course__slug=slug, year_3=True).student_capacity
                    capacity = c_model
                    print('capacity = ', capacity)
                    temp = []

                    for i in model:
                        temp.append(i)
                    print('temp : ', temp)

                    final = []
                    if len(temp) > 0:
                        for i in temp:
                            if len(final) <= int(capacity):
                                final.append(i)
                                i.selected = True
                                i.save()
                                send_mail(
                                    subject='Selection Response Mail',
                                    message='Congratulations your application for admission has been selected by our '
                                            'college authorities \n'
                                            'Here is your cutoff list link where you can check and confirm it. \n'
                                            'Here is your payment link from where you can pay fees and can confirm '
                                            'your admission seat in college.\n'
                                            'After the fees payment you will receive a mail of payment verification.',
                                    from_email='kirra000deathnote@gmail.com',
                                    recipient_list=[i.email, ],
                                    fail_silently=False,
                                )
                                i.sent_s_mail = True
                                i.save()
                    print('final : ', final)
                    print('done!')
                    return redirect('select_year_3', slug)
                else:
                    return redirect('select_year_3', slug)
            else:
                pass

        context = {
            'object_list': model,
            'form': form,
            'var': 'Select',
        }
    else:
        return HttpResponse('Student capacity of this course for year 3 has not been created.'
                            ' Please create the student capacity of this course using dashboard.')

    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/selection/select_year_3.html',
                  context=context)


class CoursesForPaymentVerify(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/imp_operations/payment_verify/course_for_payment_verify.html'


@login_required(login_url=reverse_lazy('login'))
def verify_payment(request, slug):  # Tested and PWNE
    year_1 = StudentModel.objects.filter(course__slug=slug, year_1=True, verified=True,
                                         fees_paid=False, admitted=False, selected=True, )
    year_2 = StudentModel.objects.filter(course__slug=slug, year_2=True, verified=True,
                                         fees_paid=False, admitted=False, selected=True)
    year_3 = StudentModel.objects.filter(course__slug=slug, year_3=True, verified=True,
                                         fees_paid=False, admitted=False, selected=True)

    context = {
        'year1': year_1,
        'year2': year_2,
        'year3': year_3,
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/payment_verify/paymentVerify.html',
                  context=context)


@login_required(login_url=reverse_lazy('login'))
def verify_payment_details(request, slug):  # Tested and PWNE
    model = StudentModel.objects.get(slug=slug)
    form = PaymentVerify(request.POST or request.GET or None)

    if request.method == 'POST':
        if form.is_valid():
            model.fees_paid = True
            model.save()
            send_mail(
                subject='Payment Verification Response Mail',
                message='Congratulations your fees payment has been verified by our college authorities'
                        'and send for the registration process.',
                from_email='kirra000deathnote@gmail.com',
                recipient_list=[model.email, ],
                fail_silently=False,
            )
            model.sent_p_mail = True
            model.save()

            return redirect('verify_payment', model.course.slug)
        else:
            return redirect('verify_payment', model.course.slug)

    context = {
        'object': model,
        'form': form,
        'var': 'Submit',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/payment_verify/payment_details.html',
                  context=context)


def payment_link(request, slug):  # Tested and PWNE
    form = PaymentLinkForm(request.POST or request.GET or None)
    model = StudentModel.objects.get(slug=slug)
    if request.method == 'POST':
        if form.is_valid():
            t = request.POST['transaction_id']
            d = request.POST['payment_date']
            model.transaction_id = t
            model.payment_date = d
            model.save()
            return redirect('payment_success')
        else:
            return redirect('payment_link', slug)
    context = {
        'object': model,
        'form': form,
        'var': 'Submit',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/payment link/payment_link.html',
                  context=context)


class payment_success(TemplateView):  # Tested and PWNE
    template_name = 'CRUD-temps/student-CRUD/imp_operations/payment link/payment_success.html'


class CoursesForCutoffs(ListView):  # Tested and PWNE
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/cutoff/courses_for_cutoffs.html'


def cutoffs(request, slug):  # Tested and PWNE
    year_1 = StudentModel.objects.filter(course__slug=slug, year_1=True, verified=True, selected=True)
    year_2 = StudentModel.objects.filter(course__slug=slug, year_2=True, verified=True, selected=True)
    year_3 = StudentModel.objects.filter(course__slug=slug, year_3=True, verified=True, selected=True)

    context = {
        'year1': year_1,
        'year2': year_2,
        'year3': year_3,
    }
    return render(request, template_name='CRUD-temps/student-CRUD/retrieve/cutoff/cutoffs.html',
                  context=context)


class CoursesForAdmit(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/imp_operations/registration/course_for_admit.html'


@login_required(login_url=reverse_lazy('login'))
def admit_year_1(request, slug):  # Tested and PWNE
    model = StudentModel.objects.all().filter(verified=True, year_1=True, selected=True, fees_paid=True, admitted=False)
    form = AdmitForm(request.POST or request.GET or None)
    if request.method == 'POST':
        if form.is_valid():
            for i in model:
                i.admitted = True
                send_mail(
                    subject='Admission Verification Response Mail',
                    message='Congratulations your admission has been done in our college.',
                    from_email='kirra000deathnote@gmail.com',
                    recipient_list=[i.email, ],
                    fail_silently=False,
                )
                i.sent_a_mail = True
                i.save()
            return redirect('admit_year_1', slug)
        else:
            return redirect('admit_year_1', slug)
    context = {
        'form': form,
        'object_list': model,
        'var': 'Submit',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/registration/admit_year_1.html',
                  context=context)


@login_required(login_url=reverse_lazy('login'))
def admit_year_2(request, slug):  # Tested and PWNE
    model = StudentModel.objects.all().filter(verified=True, year_2=True, selected=True, fees_paid=True, admitted=False)
    form = AdmitForm(request.POST or request.GET or None)
    if request.method == 'POST':
        if form.is_valid():
            for i in model:
                i.admitted = True
                send_mail(
                    subject='Admission Verification Response Mail',
                    message='Congratulations your admission has been done in our college.',
                    from_email='kirra000deathnote@gmail.com',
                    recipient_list=[i.email, ],
                    fail_silently=False,
                )
                i.sent_a_mail = True
                i.save()
            return redirect('admit_year_2', slug)
        else:
            return redirect('admit_year_2', slug)
    context = {
        'form': form,
        'object_list': model,
        'var': 'Submit',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/registration/admit_year_2.html',
                  context=context)


@login_required(login_url=reverse_lazy('login'))
def admit_year_3(request, slug):  # Tested and PWNE
    model = StudentModel.objects.all().filter(verified=True, year_3=True, selected=True, fees_paid=True, admitted=False)
    form = AdmitForm(request.POST or request.GET or None)
    if request.method == 'POST':
        if form.is_valid():
            for i in model:
                i.admitted = True
                send_mail(
                    subject='Admission Response Mail',
                    message='Congratulations your admission has been done in our college.',
                    from_email='kirra000deathnote@gmail.com',
                    recipient_list=[i.email, ],
                    fail_silently=False,
                )
                i.sent_a_mail = True
                i.save()
            return redirect('admit_year_3', slug)
        else:
            return redirect('admit_year_3', slug)
    context = {
        'form': form,
        'object_list': model,
        'var': 'Submit',
    }
    return render(request, template_name='CRUD-temps/student-CRUD/imp_operations/registration/admit_year_3.html',
                  context=context)


class CoursesForStudentApplication(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/applications/course_for_applications.html'


@login_required(login_url=reverse_lazy('login'))
def student_applications(request, slug):  # Tested and PWNE
    year_1 = StudentModel.objects.filter(course__slug=slug, year_1=True)
    year_2 = StudentModel.objects.filter(course__slug=slug, year_2=True)
    year_3 = StudentModel.objects.filter(course__slug=slug, year_3=True)
    context = {
        'year1': year_1,
        'year2': year_2,
        'year3': year_3,
    }
    return render(request, template_name='CRUD-temps/student-CRUD/retrieve/applications/applied_list.html',
                  context=context)


class CoursesForVerifiedStudent(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/verified/course_for_verified.html'


@login_required(login_url=reverse_lazy('login'))
def verified_students(request, slug):  # Tested and PWNE
    year_1_d = StudentModel.objects.filter(course__slug=slug, verified=True, year_1=True)
    year_2_d = StudentModel.objects.filter(course__slug=slug, verified=True, year_2=True)
    year_3_d = StudentModel.objects.filter(course__slug=slug, verified=True, year_3=True)

    year_1_p = StudentModel.objects.filter(course__slug=slug, verified=False, year_1=True)
    year_2_p = StudentModel.objects.filter(course__slug=slug, verified=False, year_2=True)
    year_3_p = StudentModel.objects.filter(course__slug=slug, verified=False, year_3=True)

    context = {
        'year_1_d': year_1_d,
        'year_2_d': year_2_d,
        'year_3_d': year_3_d,

        'year_1_p': year_1_p,
        'year_2_p': year_2_p,
        'year_3_p': year_3_p,

    }
    return render(request, template_name='CRUD-temps/student-CRUD/retrieve/verified/verified_list.html',
                  context=context)


class CoursesForFeesPaidStudent(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/fees_paid/course_for_fees_paid.html'


@login_required(login_url=reverse_lazy('login'))
def students_Fees_paid(request, slug):  # Tested and PWNE
    year_1_d = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, year_1=True)
    year_2_d = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, year_2=True)
    year_3_d = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, year_3=True)

    year_1_p = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=False, year_1=True)
    year_2_p = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=False, year_2=True)
    year_3_p = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=False, year_3=True)

    context = {
        'year_1_d': year_1_d,
        'year_2_d': year_2_d,
        'year_3_d': year_3_d,

        'year_1_p': year_1_p,
        'year_2_p': year_2_p,
        'year_3_p': year_3_p,
    }
    return render(request, template_name='CRUD-temps/student-CRUD/retrieve/fees_paid/paid.html', context=context)


class CoursesForAdmittedStudents(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = CourseModel
    template_name = 'CRUD-temps/student-CRUD/retrieve/admitted/course_for_admitted.html'


@login_required(login_url=reverse_lazy('login'))
def admitted_students(request, slug):  # Tested and PWNE
    year_1_d = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, admitted=True, year_1=True)
    year_2_d = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, admitted=True, year_2=True)
    year_3_d = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, admitted=True, year_3=True)

    year_1_p = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, admitted=False,
                                           year_1=True)
    year_2_p = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, admitted=False,
                                           year_2=True)
    year_3_p = StudentModel.objects.filter(course__slug=slug, selected=True, fees_paid=True, admitted=False,
                                           year_3=True)
    context = {
        'year_1_d': year_1_d,
        'year_2_d': year_2_d,
        'year_3_d': year_3_d,

        'year_1_p': year_1_p,
        'year_2_p': year_2_p,
        'year_3_p': year_3_p,
    }
    return render(request, template_name='CRUD-temps/student-CRUD/retrieve/admitted/admitted_list.html',
                  context=context)


# Workforce CRUD--------------------------------------------------------------------------------------------------------
class create_workforce(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = WorkForceRegistrationForm
    model = User
    template_name = 'CRUD-temps/workforce-CRUD/create.html'
    extra_context = {
        'var': 'Submit',
        'title': 'Workforce Registration',
    }
    success_url = reverse_lazy('dashboard')


class delete_workforce(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'CRUD-temps/workforce-CRUD/delete.html'
    extra_context = {
        'var': 'Delete',
        'title': 'Delete Workforce',
    }
    success_url = reverse_lazy('workforce_list')


class update_workforce(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    fields = {
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_superuser',
    }
    extra_context = {
        'var': 'Update',
        'title': 'Update Workforce',
    }
    template_name = 'CRUD-temps/workforce-CRUD/update.html'
    success_url = reverse_lazy('workforce_list')


class workforce_list(LoginRequiredMixin, ListView):  # Tested and PWNE
    login_url = reverse_lazy('login')
    model = User
    queryset = User.objects.all().filter(is_staff=True, is_superuser=False)
    template_name = 'CRUD-temps/workforce-CRUD/retrieve/list_view.html'


class workforce_detail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'CRUD-temps/workforce-CRUD/retrieve/detail_view.html'


@login_required(login_url=reverse_lazy('login'))
def change_password(request):  # Tested and PWNE
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
        'title': 'Change Password',
        'var': 'Change',
    }
    return render(request, template_name='registration/change_password.html', context=context)
