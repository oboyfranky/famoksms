from django.contrib import admin
from .models import *

# Register your models here.

# constatnts
form_input = (
    ('PERSONAL INFORMATION', {
        'fields': (
            'parent_id',
            'relation',
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
    'parent_id',
    'surname',
    'first_name',
    'other_names',
    'gender',
    )
links = ('parent_id',)
search = ['parent_id', 'gender']
filter_list = ('parent_id', 'gender',)

# level 100
class ParentProfileAdmin(admin.ModelAdmin):
    fieldsets = form_input
    list_display = display
    list_display_links = links
    search_fields = search
    list_filter = filter_list
    ordering = ['parent_id', 'gender']
admin.site.register(ParentProfile, ParentProfileAdmin)

