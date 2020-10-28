# All imports-----------------------------------------------------------------------------------------------------------
# Django imports
from django.db import models
from django.urls import reverse
from django_cleanup import cleanup


# Project imports
from django.utils.text import slugify


# All Models------------------------------------------------------------------------------------------------------------

# College Details Model # Tested and PWNE
class CollegeDetailModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, default=None)
    sub_title = models.CharField(max_length=100, null=True, blank=True, default=None)
    details = models.TextField(max_length=10000, null=False, blank=False, default=None)
    image = models.ImageField(null=True, blank=True, upload_to='Detail_Image/')
    file = models.FileField(null=True, blank=True, upload_to='Detail_File/')
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('list_college_details', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# Course Model # Tested and PWNE
class CourseModel(models.Model):
    course = models.CharField(max_length=200, null=False, blank=False, default=None)
    image = models.ImageField(upload_to='course_image/', null=True, blank=True)
    eligibility = models.TextField(max_length=5000, null=True, blank=True, default=None)
    duration_of_course = models.CharField(max_length=100, null=True, blank=True, default=None)
    syllabus = models.TextField(max_length=20000, null=True, blank=True, default=None)
    extra_details = models.TextField(max_length=50000, null=True, blank=True, default=None)
    year_1_fees = models.IntegerField(default=None, null=True, blank=True)
    year_2_fees = models.IntegerField(default=None, null=True, blank=True)
    year_3_fees = models.IntegerField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True, null=False, blank=False)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('course_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.course
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.course


# Student Capacity Model # Tested and PWNE
year = [
    ('Year 1', 'Year 1'),
    ('Year 2', 'Year 2'),
    ('Year 3', 'Year 3'),
]


class StudentCapacityModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    year_1 = models.BooleanField(default=False)
    year_2 = models.BooleanField(default=False)
    year_3 = models.BooleanField(default=False)
    student_capacity = models.IntegerField(default=None)
    active = models.BooleanField(default=True, null=False, blank=False)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('cutoff_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value1 = self.course.course
        if self.year_1:
            value2 = 'year-1'
        elif self.year_2:
            value2 = 'year-2'
        else:
            value2 = 'year-3'
        value = value1 + value2
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.course.course


# Student Model # Tested and PWNE
GenderChoices = [
    ('male', 'Male'),
    ('female', "Female"),
    ('other', 'Other',)
]

ReligionChoices = [
    ('hindu', 'Hindu'),
    ('muslim', 'Muslim'),
    ('christian', 'Christian'),
    ('other', "Other"),
]

BldChoices = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]


class StudentModel(models.Model):
    # Course Details
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    year_1 = models.BooleanField(default=False)
    year_2 = models.BooleanField(default=False)
    year_3 = models.BooleanField(default=False)

    # UID
    uid = models.IntegerField(unique=True, null=True, blank=True, default=None)

    # Personal Details
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    father_first_name = models.CharField(max_length=30, null=False, blank=False)
    mother_first_name = models.CharField(max_length=30, null=False, blank=False)

    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=50, null=False, blank=False)

    gender = models.CharField(choices=GenderChoices, blank=False, null=False, max_length=10)
    blood_group = models.CharField(null=False, blank=False, choices=BldChoices, max_length=3)

    nationality = models.CharField(null=False, blank=False, default="Indian", max_length=20)
    religion = models.CharField(null=False, blank=False, choices=ReligionChoices, max_length=20)
    mother_tongue = models.CharField(null=False, blank=False, max_length=20)

    aadhaar = models.IntegerField(blank=False, default=None)

    phone = models.IntegerField(blank=False, default=None)
    alternate_phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)

    physically_challenged = models.BooleanField(default=False)

    flat_building_street_area = models.CharField(max_length=250, null=False, blank=False, default=None)
    pincode = models.IntegerField(null=False, blank=False, default=None)
    city = models.CharField(max_length=50, null=False, blank=False, default=None)
    district = models.CharField(max_length=50, null=False, blank=False, default=None)
    tehsil = models.CharField(max_length=50, null=False, blank=False, default=None)

    # Guardian Details
    guardian_full_name = models.CharField(max_length=50, null=False, blank=False, default=None)
    guardian_phone = models.IntegerField(null=False, blank=False, default=None)
    guardian_email = models.EmailField(null=True, blank=True, default=None)
    guardian_occupation = models.CharField(max_length=20, blank=False, null=False)
    guardian_annual_income = models.IntegerField(blank=False, null=False, default=None)

    # MU Application No.
    MU_application_no = models.IntegerField(blank=False, null=False, default=None)

    # Previous Education Details
    previous_college_name = models.CharField(max_length=100, blank=False, null=False, default=None)
    previous_passing_year = models.IntegerField(blank=False, null=False, default=0000)

    SSC_percentage = models.FloatField(blank=False, null=False, default=0.0)
    HSC_percentage = models.FloatField(blank=False, null=False, default=0.0)

    semester_1_SGPI = models.FloatField(blank=False, default=0.0)
    semester_2_SGPI = models.FloatField(blank=False, default=0.0)
    semester_3_SGPI = models.FloatField(blank=False, default=0.0)
    semester_4_SGPI = models.FloatField(blank=False, default=0.0)

    aggregate_1 = models.FloatField(blank=False, default=0.0)
    aggregate_2 = models.FloatField(blank=False, default=0.0)

    # File Uploads
    photo = models.ImageField(upload_to='student_pic/', null=False, blank=False)

    SSC_mark_sheet = models.FileField(upload_to='ssc_mark_sheet', blank=False, null=False, default=None)
    HSC_mark_sheet = models.FileField(upload_to='hsc_mark_sheet', blank=False, null=False, default=None)
    previous_year_mark_sheet = models.FileField(upload_to='previous_mark_sheet', blank=False, null=False, default=None)

    leaving_certificate = models.FileField(upload_to='leaving_certificate', blank=False, null=False, default=None)

    MU_application = models.FileField(upload_to='mu_application', blank=False, null=False, default=None)

    # In/Out - House
    in_house = models.BooleanField(default=False, null=False, blank=False)
    out_house = models.BooleanField(default=False, null=False, blank=False)

    # Slug
    slug = models.SlugField(blank=True, unique=True)

    # Status
    verified = models.BooleanField(default=False)
    sent_v_mail = models.BooleanField(default=False)

    selected = models.BooleanField(default=False)
    sent_s_mail = models.BooleanField(default=False)

    transaction_id = models.IntegerField(blank=True, null=True, default=None)
    payment_date = models.DateField(null=True, blank=True, help_text='Year-Month-Day')

    fees_paid = models.BooleanField(default=False)
    sent_p_mail = models.BooleanField(default=False)

    admitted = models.BooleanField(default=False)
    sent_a_mail = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('student_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        agg_val_1 = self.semester_1_SGPI + self.semester_2_SGPI / 2
        agg_val_2 = self.semester_1_SGPI + self.semester_2_SGPI + self.semester_3_SGPI + self.semester_4_SGPI / 4
        self.aggregate_1 = agg_val_1
        self.aggregate_2 = agg_val_2
        val1 = self.name
        val2 = self.id
        value = val1 + '-' + str(val2)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
