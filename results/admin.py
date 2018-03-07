from django.contrib import admin
from .models import *

# Register your models here.

# constatnts
form_input = (
    ('STUDENTS INFORMATION', {
        'fields': (
            'student',
            'current_class',
            'option',
            'marksheet',
            )
    }),
    ('RESULTS INFORMATION', {
        'fields': (
            'subject1',
            'mark1',
            'grade1',

            'subject2',
            'mark2',
            'grade2',

            'subject3',
            'mark3',
            'grade3',

            'subject4',
            'mark4',
            'grade4',

            'subject5',
            'mark5',
            'grade5',

            'subject6',
            'mark6',
            'grade6',

            'subject7',
            'mark7',
            'grade7',

            'subject8',
            'mark8',
            'grade8',

            'subject9',
            'mark9',
            'grade9',
            )
    }),
)
display = (
    'student',
    'marksheet',
    )

# level 100
class StudentsRecordAdmin(admin.ModelAdmin):
    fieldsets = form_input
    list_display = display
    list_display_links = ('student',)
    search_fields = ['student', 'marksheet']
    list_filter = ('marksheet', 'student',)
    ordering = ['marksheet']

admin.site.register(StudentsRecord, StudentsRecordAdmin)


#------------------------------------------------------------------------------------------
class AcademicYearAdmin(admin.ModelAdmin):
    fields = ('year', 'start_date', 'end_date',)
    list_display = ('year', 'start_date', 'end_date',)
    list_display_links = ('year',)
    search_fields = ['year']
    list_filter = ('year',)
    ordering = ['-year']
admin.site.register(AcademicYear, AcademicYearAdmin)

class MarksheetAdmin(admin.ModelAdmin):
    fields = ('year', 'term', 'date',)
    list_display = ('year', 'term', 'date',)
    search_fields = ['year', 'term', 'date']
    list_filter = ('year', 'term', 'date')
    ordering = ['-year', '-term', 'date']
admin.site.register(Marksheet, MarksheetAdmin)