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
TYPE = (
	('Head Master / Mistress', 'Head Master / Mistress'),
	('Ass. Head Master / Mistress', 'Ass. Head Master / Mistress'),
	)

class AdministrationProfile(models.Model):
	# PERSONAL INFO AND CURRICULAR
	admin_id = models.CharField('Administration Id', max_length = 15, unique = True)
	surname = models.CharField('Surname', max_length=50)
	first_name = models.CharField('First Name', max_length=50)
	other_names = models.CharField('Other Names', max_length=50, null=True, blank=True)
	gender = models.CharField('Gender / Sex', max_length=50, choices=GENDER)
	title = models.CharField('Title', max_length=50, choices=TITLE)
	hiredate = models.DateField('Hire Date')
	admin_type = models.CharField('Administration Type', max_length=50, choices=TYPE)
	photo = models.ImageField('Profile Image', upload_to = 'photos')
	post_address = models.CharField('Postal Address', max_length=100)
	home_address = models.CharField('Home Address', max_length=100)

	class Meta:
		verbose_name = 'Administration Profile' 
		verbose_name_plural = 'Administration Profile'

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
		if self.admin_id:
		    admin_id = " - " + self.admin_id

		return u"%s %s %s" % (surname.upper(), first_name.upper(), admin_id)

	def get_absolute_url_admin_profile_details(self):
		return reverse('administration:admin_profile_details', args={self.id})