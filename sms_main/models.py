from django.db import models
from django.core.urlresolvers import reverse
from student.models import StudentProfile 
# Create your models here.
# CONSTANTS
TARGET = (
	('Students', 'Students'),
	('Parents', 'Parents'),
	('Teachers', 'Teachers'),
	('Administration', 'Administration'),
	('Accountant', 'Accountant'),
	)

SUBSCRIBE = (
	('Thanks for your usual cooperation', 'Thanks for your usual cooperation'),
	('Thank You', 'Thank You'),
	)

CLASS = (
	('Form 1', 'Form 1'),
	('Form 2', 'Form 2'),
	('Form 3', 'Form 3'),
	('Old Students', 'Old Students'),
	)

OPTIONS = (
	('--------------', '--------------'),
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
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

TERM = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	)

STATUS = (
	('Paid', 'Paid'),
	('Not Paid', 'Not Paid'),
	)


class NoticeInfo(models.Model):
	# PERSONAL INFO AND CURRICULAR
	audience = models.CharField('Audience', max_length = 50, choices = TARGET)
	title = models.CharField('Notice Title', max_length = 50)
	content = models.TextField('Notice Body')
	submitted = models.DateField('Submitted', auto_now_add = True)
	updated = models.DateField('Updated', auto_now = True)
	subscribe = models.CharField('Subscribe', max_length = 50, choices = SUBSCRIBE, default = 'Thank You')

	class Meta:
		verbose_name = 'Notice Info' 
		verbose_name_plural = 'Notice Info'

	def __str__(self):
		return self.title

	def get_absolute_url_secretary_not(self):
		return reverse('secretary:notice_details', args={self.id})

	def get_absolute_url_administration_not(self):
		return reverse('administration:notice_details', args={self.id})

class ClassInfo(models.Model):
	# PERSONAL INFO AND CURRICULAR
	name = models.CharField('Class', max_length = 50, choices = CLASS)
	option = models.CharField('Class Option', max_length=100, choices=OPTIONS, default = '--------------')

	class Meta:
		verbose_name = 'Class Info' 
		verbose_name_plural = 'Class Info'

	def __str__(self):
		name = ""
		option = ""
		if self.name:
		    name = self.name
		if self.option:
		    option = self.option

		return u"%s %s" % (name, option)


class StudentFinance(models.Model):
	year = models.CharField('Year', max_length=50)
	term = models.CharField('Term', max_length=100, choices=TERM)
	student = models.ForeignKey(StudentProfile, on_delete = models.CASCADE, null=True, blank=True)
	school_class = models.ForeignKey(ClassInfo, on_delete = models.CASCADE)
	amount = models.CharField('Amount to be Paid GHc', max_length=100)
	paid = models.CharField('Amount Paid GHc', max_length=100)
	date = models.DateField('Date', auto_now_add = True)
	status = models.CharField('Payment Status', max_length=100, choices=STATUS)

	class Meta:
		verbose_name = 'Student Financial Status'
		verbose_name_plural = 'Student Financial Status'

	def __str__(self):
		return u"%s - %s" %(self.year, self.term)


class SchoolIncome(models.Model):
	year = models.CharField('Year', max_length=50)
	term = models.CharField('Term', max_length=100, choices=TERM)
	name = models.CharField('Title', max_length=100, null = True, blank = True)
	content = models.TextField('Details', null = True, blank = True)
	paid = models.CharField('Amount GHc', max_length=100)
	date = models.DateField('Date', auto_now_add = True)

	class Meta:
		verbose_name = 'School Income'
		verbose_name_plural = 'School Income'

	def __str__(self):
		return self.year

	def get_absolute_url_income(self):
		return reverse('administration:income_details', args={self.id})


class SchoolExpenses(models.Model):
	year = models.CharField('Year', max_length=50)
	term = models.CharField('Term', max_length=100, choices=TERM)
	name = models.CharField('Title', max_length=100, null = True, blank = True)
	content = models.TextField('Details', null = True, blank = True)
	paid = models.CharField('Amount GHc', max_length=100)
	date = models.DateField('Date', auto_now_add = True)

	class Meta:
		verbose_name = 'School Expenses'
		verbose_name_plural = 'School Expenses'

	def __str__(self):
		return self.year

	def get_absolute_url_expense(self):
		return reverse('administration:expense_details', args={self.id})


class SubjectInfo(models.Model):
	# PERSONAL INFO AND CURRICULAR
	school_class = models.ForeignKey(ClassInfo, on_delete = models.CASCADE)
	subject = models.CharField('Subject', max_length =50, choices = SUBJECTS)
	mark = models.CharField('Total Mark', max_length=100)
	
	
	class Meta:
		verbose_name = 'Subject Info' 
		verbose_name_plural = 'Subject Info'

	def __str__(self):
		return self.subject


class Messages(models.Model):
	sender_id = models.CharField("Sender Id", max_length = 50)
	sender_name = models.CharField("Sender Name", max_length = 50)
	reciever_id = models.CharField("Reciepient Id", max_length = 50)
	reciever_name = models.CharField("Reciepient Name", max_length = 50)
	subject = models.CharField("Subject", max_length = 50)
	message = models.TextField("Message")
	sent = models.DateTimeField("Date Sent", auto_now_add = True)

	class Meta:
		verbose_name = 'Messages'
		verbose_name_plural = 'Messages'

	def __str__(self):
		return self.sender_id

	def get_absolute_url_student_mgs(self):
		return reverse('student:messages_details', args={self.id})

	def get_absolute_url_student_send(self):
		return reverse('student:send_details', args={self.id})

	def get_absolute_url_parent_mgs(self):
		return reverse('parent:messages_details', args={self.id})

	def get_absolute_url_parent_send(self):
		return reverse('parent:send_details', args={self.id})

	def get_absolute_url_teacher_mgs(self):
		return reverse('teacher:messages_details', args={self.id})

	def get_absolute_url_teacher_send(self):
		return reverse('teacher:send_details', args={self.id})

	def get_absolute_url_staff_mgs(self):
		return reverse('staff:messages_details', args={self.id})

	def get_absolute_url_staff_send(self):
		return reverse('staff:send_details', args={self.id})

	def get_absolute_url_accountant_mgs(self):
		return reverse('accountant:messages_details', args={self.id})

	def get_absolute_url_accountant_send(self):
		return reverse('accountant:send_details', args={self.id})

	def get_absolute_url_secretary_mgs(self):
		return reverse('secretary:messages_details', args={self.id})

	def get_absolute_url_secretary_send(self):
		return reverse('secretary:send_details', args={self.id})

	def get_absolute_url_administration_mgs(self):
		return reverse('administration:messages_details', args={self.id})

	def get_absolute_url_administration_send(self):
		return reverse('administration:send_details', args={self.id})