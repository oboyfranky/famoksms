from django.contrib import admin
from .models import *

# Register your models here.

# constatnts
form_input = (
    ('CURRICULAR', {
        'fields': (
            'admin_id',
            'admin_type',
            'hiredate',
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
    'admin_id',
    'surname',
    'first_name',
    'other_names',
    'gender',
    'hiredate',
    'admin_type',
    )
links = ('admin_id',)
search = ['admin_id', 'gender', 'hiredate', 'admin_type']
filter_list = ('admin_id', 'gender', 'hiredate', 'admin_type',)

class AdministrationProfileAdmin(admin.ModelAdmin):
    fieldsets = form_input
    list_display = display
    list_display_links = links
    search_fields = search
    list_filter = filter_list
    ordering = ['admin_id', 'gender']
admin.site.register(AdministrationProfile, AdministrationProfileAdmin)

