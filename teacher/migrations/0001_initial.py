# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach_id', models.CharField(max_length=15, unique=True, verbose_name='Teacher Id')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('other_names', models.CharField(blank=True, max_length=50, null=True, verbose_name='Other Names')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50, verbose_name='Gender / Sex')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Miss')], max_length=50, verbose_name='Title')),
                ('subject', models.CharField(choices=[('Mathematics', 'Mathematics'), ('Social Studies', 'Social Studies'), ('Integrated Science', 'Integrated Science'), ('English Language', 'English Language'), ('Religious and Moral Education', 'Religious and Moral Education'), ('Fantse', 'Fantse'), ('French', 'French'), ('BDT Technical', 'BDT Technical'), ('BDT Home Econoomics', 'BDT Home Econoomics')], max_length=50, verbose_name='Subject')),
                ('hiredate', models.DateField(verbose_name='Hire Date')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Profile Image')),
                ('post_address', models.CharField(max_length=100, verbose_name='Postal Address')),
                ('home_address', models.CharField(max_length=100, verbose_name='Home Address')),
            ],
            options={
                'verbose_name': 'Teachers Profile',
                'verbose_name_plural': 'Teachers Profile',
            },
        ),
    ]
