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
RELATION = (
	('Father', 'Father'),
	('Mother', 'Mother'),
	('Uncle', 'Uncle'),
	('Aunt', 'Aunt'),
	('Other', 'Other'),
	)
GENDER = (
	('M', 'Male'),
	('F', 'Female'),
	)


# tables

# level 100
class ParentProfile(models.Model):
	# PERSONAL INFO AND CURRICULAR
	parent_id = models.CharField('Parent Id', max_length = 15, unique = True)
	surname = models.CharField('Surname', max_length=50)
	first_name = models.CharField('First Name', max_length=50)
	other_names = models.CharField('Other Names', max_length=50, null=True, blank=True)
	gender = models.CharField('Gender / Sex', max_length=50, choices=GENDER)
	title = models.CharField('Title', max_length=50, choices=TITLE)
	relation = models.CharField('Relation', max_length=50, choices=RELATION)
	photo = models.ImageField('Profile Image', upload_to = 'photos')
	post_address = models.CharField('Postal Address', max_length=100)
	home_address = models.CharField('Home Address', max_length=100)

	class Meta:
		verbose_name = 'Parents Profile'
		verbose_name_plural = 'Parents Profile'

	def __str__(self):
		first_name = ""
		surname = ""
		if self.first_name:
		    first_name = self.first_name
		if self.surname:
		    surname = self.surname + ","
		if self.parent_id:
		    parent_id = " - " + self.parent_id

		return u"%s %s %s" % (surname.upper(), first_name.upper(), parent_id)

	def get_absolute_url_admin_par_profile_details(self):
		return reverse('administration:par_profile_details', args={self.id})


