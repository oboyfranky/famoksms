# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_id', models.CharField(max_length=50, unique=True, verbose_name='Student Id')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('other_names', models.CharField(blank=True, max_length=50, null=True, verbose_name='Other Names')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50, verbose_name='Gender / Sex')),
                ('admission_year', models.CharField(max_length=50, verbose_name='Admission Year')),
                ('admitted_class', models.CharField(choices=[('Form 1', 'Form 1'), ('Form 2', 'Form 2'), ('Form 3', 'Form 3'), ('Old Students', 'Old Students')], max_length=50, verbose_name='Admitted Class')),
                ('current_class', models.CharField(choices=[('Form 1', 'Form 1'), ('Form 2', 'Form 2'), ('Form 3', 'Form 3'), ('Old Students', 'Old Students')], max_length=50, verbose_name='Current Class')),
                ('option', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, verbose_name='Class Option')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Profile Image')),
                ('post_address', models.CharField(max_length=100, verbose_name='Postal Address')),
                ('home_address', models.CharField(max_length=100, verbose_name='Home Address')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parent.ParentProfile')),
            ],
            options={
                'verbose_name': 'Students Profile',
                'verbose_name_plural': 'Students Profile',
            },
        ),
    ]