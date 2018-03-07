from django.contrib import admin
from .models import *

# Register your models here.

# constatnts
form_input = (
    ('CURRICULAR', {
        'fields': (
            'stud_id',
            'admission_year',
            'admitted_class',
            'current_class',
            'option',
            )
    }),
    ('PERSONAL INFORMATION', {
        'fields': (
            'surname',
            'first_name',
            'other_names',
            'gender',
            'photo',
            'date_of_birth',
            'post_address' ,
            'home_address',
            'parent'
            )
    }),
)
display = (
    'stud_id',
    'surname',
    'first_name',
    'other_names',
    'admission_year',
    'admitted_class',
    'current_class',
    'option',
    )
links = ('stud_id',)
search = ['stud_id', 'gender', 'admission_year', 'current_class', 'option']
filter_list = ('stud_id', 'gender', 'admission_year', 'current_class', 'option',)

# level 100
class StudentProfileAdmin(admin.ModelAdmin):
    fieldsets = form_input
    list_display = display
    list_display_links = links
    search_fields = search
    list_filter = filter_list
    ordering = ['current_class', 'admission_year']
    actions = ['form_1', 'form_2', 'form_3', 'old_student']


    def form_1(self, request, queryset):
        promote = queryset.update(current_class = 'Form 1')
        if promote == 1:
            message = '1 Student was'
        else:
            message = '%s Students were' %s (promote)

        self.message_user(request, '%s Promoted.' % message)

    form_1.short_description = "Promote to Form 1"

    def form_2(self, request, queryset):
        promote = queryset.update(current_class = 'Form 2')
        if promote == 1:
            message = '1 Student was'
        else:
            message = '%s Students were' %s (promote)

        self.message_user(request, '%s Promoted.' % message)

    form_2.short_description = "Promote to Form 2"

    def form_3(self, request, queryset):
        promote = queryset.update(current_class = 'Form 3')
        if promote == 1:
            message = '1 Student was'
        else:
            message = '%s Students were' %s (promote)

        self.message_user(request, '%s Promoted.' % message)

    form_3.short_description = "Promote to Form 3"

    def old_student(self, request, queryset):
        promote = queryset.update(current_class = 'Old Students')
        if promote == 1:
            message = '1 Student was'
        else:
            message = '%s Students were' %s (promote)

        self.message_user(request, '%s Promoted.' % message)

    old_student.short_description = "Add to Old Students"

admin.site.register(StudentProfile, StudentProfileAdmin)