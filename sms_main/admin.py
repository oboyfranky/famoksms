from django.contrib import admin
from .models import *

# Register your models here.
class NoticeInfoAdmin(admin.ModelAdmin):
    fields = ('audience', 'title', 'content', 'subscribe',)
    list_display = ('audience', 'title', 'content', 'submitted', 'updated',)
    list_display_links = ('title',)
    search_fields = ['title', 'audience']
    list_filter = ('title', 'audience')
    ordering = ['-updated', '-submitted', 'audience']
admin.site.register(NoticeInfo, NoticeInfoAdmin)

class ClassInfoAdmin(admin.ModelAdmin):
    fields = ('name', 'option',)
    list_display = ('name', 'option',)
    list_display_links = ('name',)
    search_fields = ['name', 'option']
    list_filter = ('name', 'option',)
    ordering = ['name', 'option']
admin.site.register(ClassInfo, ClassInfoAdmin)


class SubjectInfoAdmin(admin.ModelAdmin):
    form_input = (
        ('CLASS', {
            'fields': (
                'school_class',
                'subject',
                'mark',
                )
        }),
    )
    list_display = (
        'school_class', 
        'subject',
        'mark',
        )
    list_display_links = ('school_class',)
    search_fields = ['school_class', 'subject']
    list_filter = ('school_class', 'subject')
    ordering = ['school_class']
admin.site.register(SubjectInfo, SubjectInfoAdmin)


class MessagesAdmin(admin.ModelAdmin):
    fields = ('sender_id', 'sender_name', 'reciever_id', 'reciever_name', 'subject', 'message',)
    list_display = ('sender_id', 'sender_name', 'reciever_id', 'reciever_name', 'sent',)
    list_display_links = ('sender_id',)
    search_fields = ['sender_id', 'sender_name', 'reciever_id', 'reciever_name', 'sent',]
    list_filter = ('sender_id', 'sender_name', 'reciever_id', 'reciever_name', 'sent',)
    ordering = ['-sent']
admin.site.register(Messages, MessagesAdmin)


class StudentFinanceAdmin(admin.ModelAdmin):
    fields = (
        'year',
        'term',
        'student',
        'school_class',
        'amount',
        'paid',
        'status',
        )
    list_display = (
        'student',
        'year',
        'term',
        'amount',
        'paid',
        'date',
        'status',
        )
    list_display_links = ('student',)
    search_fields = ['year', 'term', 'student', 'status', 'school_class', 'date']
    list_filter = ('year', 'term', 'student', 'status', 'school_class', 'date',)
    ordering = ['year', 'term', 'school_class', 'date']
admin.site.register(StudentFinance, StudentFinanceAdmin)


class SchoolIncomeAdmin(admin.ModelAdmin):
    fields = (
        'year',
        'term',
        'name',
        'content',
        'paid',
        'date',
        )
    list_display = (
        'year',
        'term',
        'name',
        'date',
        )
    list_display_links = ('year',)
    search_fields = ['year', 'term', 'date']
    list_filter = ('year', 'term', 'date',)
    ordering = ['-year', '-term']
admin.site.register(SchoolIncome, SchoolIncomeAdmin)


class SchoolExpensesAdmin(admin.ModelAdmin):
    fields = (
        'year',
        'term',
        'name',
        'content',
        'paid',
        'date',
        )
    list_display = (
        'year',
        'term',
        'name',
        'date',
        )
    list_display_links = ('year',)
    search_fields = ['year', 'term', 'date']
    list_filter = ('year', 'term', 'date',)
    ordering = ['year', 'term']
admin.site.register(SchoolExpenses, SchoolExpensesAdmin)