from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image

# Create your models here.
# CONSTANTS
TITLE = (
	('Mr', 'Mr'),
	('Mrs', 'Mrs'),
	('Ms', 'Miss'),
	)
GENDER = (
	('M', 'Male'),
	('F', 'Female'),
	)

SUBJECTS = (
	('Mathematics', 'Mathematics'),
	('Social Studies', 'Social Studies'),
	('Integrated Science', 'Integrated Science'),
	('English Language', 'English Language'),
	('Religious and Moral Education', 'Religious and Moral Education'),
	('Fantse', 'Fantse'),
	('French', 'French'),
	('BDT Technical', 'BDT Technical'),
	('BDT Home Econoomics', 'BDT Home Econoomics'),
	)


class TeacherProfile(models.Model):
	# PERSONAL INFO AND CURRICULAR
	teach_id = models.CharField('Teacher Id', max_length = 15, unique = True)
	surname = models.CharField('Surname', max_length=50)
	first_name = models.CharField('First Name', max_length=50)
	other_names = models.CharField('Other Names', max_length=50, null=True, blank=True)
	gender = models.CharField('Gender / Sex', max_length=50, choices=GENDER)
	title = models.CharField('Title', max_length=50, choices=TITLE)
	subject = models.CharField('Subject', max_length=50, choices=SUBJECTS)
	hiredate = models.DateField('Hire Date')
	photo = models.ImageField('Profile Image', upload_to = 'photos')
	post_address = models.CharField('Postal Address', max_length=100)
	home_address = models.CharField('Home Address', max_length=100)

	class Meta:
		verbose_name = 'Teachers Profile' 
		verbose_name_plural = 'Teachers Profile'

	def __str__(self):
		first_name = ""
		other_names = ""
		surname = ""
		if self.first_name:
		    first_name = self.first_name
		if self.other_names:
		    other_names = self.other_names
		if self.surname:
		    surname = self.surname + ","
		if self.teach_id:
		    teach_id = " - " + self.teach_id

		return u"%s %s %s" % (surname.upper(), first_name.upper(), teach_id)

	def get_absolute_url_admin_tea_profile_details(self):
		return reverse('administration:tea_profile_details', args={self.id})


