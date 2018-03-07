# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Form 1', 'Form 1'), ('Form 2', 'Form 2'), ('Form 3', 'Form 3'), ('Old Students', 'Old Students')], max_length=50, verbose_name='Class')),
                ('option', models.CharField(choices=[('--------------', '--------------'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='--------------', max_length=100, verbose_name='Class Option')),
            ],
            options={
                'verbose_name': 'Class Info',
                'verbose_name_plural': 'Class Info',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.CharField(max_length=50, verbose_name='Sender Id')),
                ('sender_name', models.CharField(max_length=50, verbose_name='Sender Name')),
                ('reciever_id', models.CharField(max_length=50, verbose_name='Reciepient Id')),
                ('reciever_name', models.CharField(max_length=50, verbose_name='Reciepient Name')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('sent', models.DateTimeField(auto_now_add=True, verbose_name='Date Sent')),
            ],
            options={
                'verbose_name': 'Messages',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='NoticeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience', models.CharField(choices=[('Students', 'Students'), ('Parents', 'Parents'), ('Teachers', 'Teachers'), ('Administration', 'Administration'), ('Accountant', 'Accountant')], max_length=50, verbose_name='Audience')),
                ('title', models.CharField(max_length=50, verbose_name='Notice Title')),
                ('content', models.TextField(verbose_name='Notice Body')),
                ('submitted', models.DateField(auto_now_add=True, verbose_name='Submitted')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('subscribe', models.CharField(choices=[('Thanks for your usual cooperation', 'Thanks for your usual cooperation'), ('Thank You', 'Thank You')], default='Thank You', max_length=50, verbose_name='Subscribe')),
            ],
            options={
                'verbose_name': 'Notice Info',
                'verbose_name_plural': 'Notice Info',
            },
        ),
        migrations.CreateModel(
            name='SchoolExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, verbose_name='Year')),
                ('term', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100, verbose_name='Term')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('paid', models.CharField(max_length=100, verbose_name='Amount GHc')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'School Expenses',
                'verbose_name_plural': 'School Expenses',
            },
        ),
        migrations.CreateModel(
            name='SchoolIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, verbose_name='Year')),
                ('term', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100, verbose_name='Term')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('paid', models.CharField(max_length=100, verbose_name='Amount GHc')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'School Income',
                'verbose_name_plural': 'School Income',
            },
        ),
        migrations.CreateModel(
            name='StudentFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, verbose_name='Year')),
                ('term', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100, verbose_name='Term')),
                ('amount', models.CharField(max_length=100, verbose_name='Amount to be Paid GHc')),
                ('paid', models.CharField(max_length=100, verbose_name='Amount Paid GHc')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=100, verbose_name='Payment Status')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_main.ClassInfo')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.StudentProfile')),
            ],
            options={
                'verbose_name': 'Student Financial Status',
                'verbose_name_plural': 'Student Financial Status',
            },
        ),
        migrations.CreateModel(
            name='SubjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Mathematics', 'Mathematics'), ('Social Studies', 'Social Studies'), ('Integrated Science', 'Integrated Science'), ('English Language', 'English Language'), ('Religious and Moral Education', 'Religious and Moral Education'), ('Fantse', 'Fantse'), ('French', 'French'), ('BDT Technical', 'BDT Technical'), ('BDT Home Econoomics', 'BDT Home Econoomics')], max_length=50, verbose_name='Subject')),
                ('mark', models.CharField(max_length=100, verbose_name='Total Mark')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_main.ClassInfo')),
            ],
            options={
                'verbose_name': 'Subject Info',
                'verbose_name_plural': 'Subject Info',
            },
        ),
    ]
