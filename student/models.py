from django.db import models
from django.core.urlresolvers import reverse
from parent.models import ParentProfile 
from .models import *
from PIL import Image

# Create your models here.
# CONSTANTS
CLASS = (
	('Form 1', 'Form 1'),
	('Form 2', 'Form 2'),
	('Form 3', 'Form 3'),
	('Old Students', 'Old Students'),
	)

GENDER = (
	('M', 'Male'),
	('F', 'Female'),
	)

OPTIONS = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
	)

# tables

# level 100
class StudentProfile(models.Model):
	# PERSONAL INFO AND CURRICULAR
	parent = models.ForeignKey(ParentProfile, on_delete = models.CASCADE, null=True, blank=True)
	stud_id = models.CharField('Student Id', max_length = 50, unique = True)
	surname = models.CharField('Surname', max_length=50)
	first_name = models.CharField('First Name', max_length=50)
	other_names = models.CharField('Other Names', max_length=50, null=True, blank=True)
	gender = models.CharField('Gender / Sex', max_length=50, choices=GENDER)
	admission_year = models.CharField('Admission Year', max_length=50)
	admitted_class = models.CharField('Admitted Class', max_length=50, choices=CLASS)
	current_class = models.CharField('Current Class', max_length=50, choices=CLASS)
	option = models.CharField('Class Option', max_length=100, choices=OPTIONS)
	date_of_birth = models.DateField('Date of Birth')
	photo = models.ImageField('Profile Image', upload_to = 'photos')
	post_address = models.CharField('Postal Address', max_length=100)
	home_address = models.CharField('Home Address', max_length=100)

	class Meta:
		verbose_name = 'Students Profile'
		verbose_name_plural = 'Students Profile'

	def __str__(self):
		first_name = ""
		other_names = ""
		surname = ""
		stud_id = ""
		if self.first_name:
		    first_name = self.first_name
		if self.other_names:
		    other_names = self.other_names
		if self.surname:
		    surname = self.surname + ","
		if self.stud_id:
		    stud_id = " - " + self.stud_id

		return u"%s %s %s %s" % (surname.upper(), first_name.upper(), other_names.upper(), stud_id)

	def get_absolute_url_admin_stud_profile_details(self):
		return reverse('administration:stud_profile_details', args={self.id})

	def get_absolute_url_tea_stud_profile_details(self):
		return reverse('teacher:stud_profile_details', args={self.id})


