from django.contrib import admin
from .models import *

# Register your models here.

# constatnts
form_input = (
    ('CURRICULAR', {
        'fields': (
            'teach_id',
            'hiredate',
            'subject',
            )
    }),
    ('PERSONAL INFORMATION', {
        'fields': (
        	'title',
            'surname',
            'first_name',
            'other_names',
            'gender',
            'photo',
            'post_address' ,
            'home_address',
            )
    }),
)
display = (
    'teach_id',
    'surname',
    'first_name',
    'other_names',
    'subject',
    'gender',
    'hiredate',
    )
links = ('teach_id',)
search = ['teach_id', 'gender', 'hiredate']
filter_list = ('teach_id', 'gender', 'hiredate',)

# level 100
class TeacherProfileAdmin(admin.ModelAdmin):
    fieldsets = form_input
    list_display = display
    list_display_links = links
    search_fields = search
    list_filter = filter_list
    ordering = ['teach_id', 'gender']
admin.site.register(TeacherProfile, TeacherProfileAdmin)

