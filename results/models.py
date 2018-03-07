from django.db import models
from django.core.urlresolvers import reverse
from student.models import StudentProfile 

# Create your models here.
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

CLASS = (
	('Form 1', 'Form 1'),
	('Form 2', 'Form 2'),
	('Form 3', 'Form 3'),
	)

OPTIONS = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
	)

class AcademicYear(models.Model):
	year = models.IntegerField()
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)

	class Meta:
		verbose_name = 'Academic Year'
		verbose_name_plural = 'Academic Year'

	def __str__(self):
	    return u"%s-%s" % (self.year, str(self.year + 1)[-2:])


class Marksheet(models.Model):
	year = models.ForeignKey(AcademicYear, on_delete = models.CASCADE)
	term = models.IntegerField('Term', blank=True, null=True)
	date = models.DateField('Date', blank=True, null=True)

	class Meta:
		verbose_name = 'Marksheet'
		verbose_name_plural = 'Marksheet'

	def __str__(self):
	    return u"%s / Term %s" %(self.year, self.term)


class StudentsRecord(models.Model):
	marksheet = models.ForeignKey(Marksheet, on_delete = models.CASCADE)
	student = models.ForeignKey(StudentProfile, on_delete = models.CASCADE, null=True, blank=True)
	current_class = models.CharField('Class', max_length=50, choices = CLASS)
	option = models.CharField('Class Option', max_length=50, choices = OPTIONS)

	subject1 = models.CharField('Subject 1', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark1 = models.IntegerField('Student Mark', null=True, blank=True)
	grade1 = models.IntegerField('Student Grade', null=True, blank=True)

	subject2 = models.CharField('Subject 2', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark2 = models.IntegerField('Student Mark', null=True, blank=True)
	grade2 = models.IntegerField('Student Grade', null=True, blank=True)

	subject3 = models.CharField('Subject 3', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark3 = models.IntegerField('Student Mark', null=True, blank=True)
	grade3 = models.IntegerField('Student Grade', null=True, blank=True)

	subject4 = models.CharField('Subject 4', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark4 = models.IntegerField('Student Mark', null=True, blank=True)
	grade4 = models.IntegerField('Student Grade', null=True, blank=True)

	subject5 = models.CharField('Subject 5', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark5 = models.IntegerField('Student Mark', null=True, blank=True)
	grade5 = models.IntegerField('Student Grade', null=True, blank=True)

	subject6 = models.CharField('Subject 6', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark6 = models.IntegerField('Student Mark', null=True, blank=True)
	grade6 = models.IntegerField('Student Grade', null=True, blank=True)

	subject7 = models.CharField('Subject 7', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark7 = models.IntegerField('Student Mark', null=True, blank=True)
	grade7 = models.IntegerField('Student Grade', null=True, blank=True)

	subject8 = models.CharField('Subject 8', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark8 = models.IntegerField('Student Mark', null=True, blank=True)
	grade8 = models.IntegerField('Student Grade', null=True, blank=True)

	subject9 = models.CharField('Subject 9', max_length =50, choices = SUBJECTS, null=True, blank=True)
	mark9 = models.IntegerField('Student Mark', null=True, blank=True)
	grade9 = models.IntegerField('Student Grade', null=True, blank=True)


	class Meta:
		verbose_name = 'All Students Record'
		verbose_name_plural = 'All Students Record'

	def __str__(self):
		return self.current_class


	def get_absolute_url_student_results(self):
		return reverse('student:results_details', args={self.id})

	def get_absolute_url_par_student_results(self):
		return reverse('parent:results_details', args={self.id})

	def get_absolute_url_tea_student_results(self):
		return reverse('teacher:stud_results_details', args={self.id})

	def get_absolute_url_admin_student_results(self):
		return reverse('administration:results_details', args={self.id})


