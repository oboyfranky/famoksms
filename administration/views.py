from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AdministrationProfile
from student.models import StudentProfile
from parent.models import ParentProfile
from teacher.models import TeacherProfile
from sms_main.models import Messages, NoticeInfo, StudentFinance, SchoolIncome, SchoolExpenses
from results.models import AcademicYear, StudentsRecord

# Create your views here.
@login_required
def dashboard(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	user_messages = Messages.objects.all().filter(reciever_id = username).order_by('-sent')[:2]
	user_notice = NoticeInfo.objects.all().filter(audience = 'Administration').order_by('-submitted')[:1]
	template_name = 'administration/dashboard.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'user_messages' : user_messages,
	    'user_notice' : user_notice
	}
	
	return render(request, template_name, context)

@login_required
def profile(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	template_name = 'administration/profile.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username
	}
	
	return render(request, template_name, context)


@login_required
def stud_profile(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	students = StudentProfile.objects.all().order_by('current_class')
	template_name = 'administration/stud_profile.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'students' : students
	}
	
	return render(request, template_name, context)

@login_required
def stud_profile_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	students_det = get_object_or_404(StudentProfile, id=id)
	template_name = 'administration/stud_profile_details.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'students_det' : students_det
	}
	
	return render(request, template_name, context)


@login_required
def parents(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	parent = ParentProfile.objects.all()
	template_name = 'administration/parents.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'parent' : parent
	}
	
	return render(request, template_name, context)

@login_required
def par_profile_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	parent_det = get_object_or_404(ParentProfile, id=id)
	template_name = 'administration/par_profile_details.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'parent_det' : parent_det
	}
	
	return render(request, template_name, context)


@login_required
def teachers(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	teacher = TeacherProfile.objects.all()
	template_name = 'administration/teachers.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'teacher' : teacher
	}
	
	return render(request, template_name, context)


@login_required
def tea_profile_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	teacher_det = get_object_or_404(TeacherProfile, id=id)
	template_name = 'administration/tea_profile_details.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'teacher_det' : teacher_det
	}
	
	return render(request, template_name, context)


@login_required
def secretary(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	secretary = SecretaryProfile.objects.all()
	template_name = 'administration/secretary.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'secretary' : secretary
	}
	
	return render(request, template_name, context)


@login_required
def sec_profile_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	sec_det = get_object_or_404(SecretaryProfile, id=id)
	template_name = 'administration/sec_profile_details.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'sec_det' : sec_det
	}
	
	return render(request, template_name, context)


@login_required
def notice(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	notice = NoticeInfo.objects.all().order_by('-submitted')

	if request.method == 'POST':
		target = request.POST['audience']
		title = request.POST['title']
		body = request.POST['body']

		post = NoticeInfo(
			audience = target,
			title = title,
			content = body,
			)
		post.save()
		return redirect('/administration/notice', {'info' : 'message sent successfuly'})

	template_name = 'administration/notice.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'notice' : notice
	}
	
	return render(request, template_name, context)

@login_required
def notice_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	notice_det = get_object_or_404(NoticeInfo, id=id)

	template_name = 'administration/notice_details.html'
	context = {
	    'admin_profile' : query,
	    'notice_det' : notice_det,
	    'admin_id': username
	}
	return render(request, template_name, context)


@login_required
def messages(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	user_messages = Messages.objects.all().filter(reciever_id = username).order_by('-sent')

	if request.method == 'POST':
		recipient_id = request.POST['recipient_id']
		reciever_name = request.POST['reciever_name']
		sender_name = request.POST['sender_name']
		subject = request.POST['subject']
		body = request.POST['body']

		chat = Messages(
			sender_id = username,
			sender_name = sender_name,
			reciever_id = recipient_id,
			reciever_name = reciever_name,
			subject = subject,
			message = body,
			)
		chat.save()
		return redirect('/administration/send', {'info' : 'message sent successfuly'})
		#reverse_lazy('send')

	template_name = 'administration/messages.html'
	context = {
	    'admin_profile' : query,
	    'user_messages' : user_messages,
	    'admin_id': username
	}
	return render(request, template_name, context)

@login_required
def messages_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	message_det = get_object_or_404(Messages, id=id)

	template_name = 'administration/messages_details.html'
	context = {
	    'admin_profile' : query,
	    'message_det' : message_det,
	    'admin_id': username
	}
	return render(request, template_name, context)


@login_required
def send(request):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	user_sent = Messages.objects.all().filter(sender_id = username).order_by('-sent')

	template_name = 'administration/sent.html'
	context = {
	    'admin_profile' : query,
	    'user_sent' : user_sent,
	    'admin_id': username
	}
	return render(request, template_name, context)

@login_required
def send_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	sent_det = get_object_or_404(Messages, id=id)

	template_name = 'administration/sent_details.html'
	context = {
	    'admin_profile' : query,
	    'sent_det' : sent_det,
	    'admin_id': username
	}
	return render(request, template_name, context)

@login_required
def finance(request):
	user = request.user
	username = user.username
	template_name = 'administration/finance.html'
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	student_finance = StudentFinance.objects.all().order_by('-date')
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'student_finance' : student_finance
	}
	
	return render(request, template_name, context)

@login_required
def income(request):
	user = request.user
	username = user.username
	template_name = 'administration/income.html'
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	income = SchoolIncome.objects.all().order_by('-date')

	if request.method == 'POST':
		year = request.POST['year']
		term = request.POST['term']
		title = request.POST['title']
		body = request.POST['body']

		income = SchoolIncome(
			year = year,
			term = term,
			name = title,
			content = body,
			)
		income.save()
		return redirect('/administration/income', {'info' : 'message sent successfuly'})

	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'income' : income
	}
	
	return render(request, template_name, context)


@login_required
def income_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	income_dets = get_object_or_404(SchoolIncome, id=id)

	template_name = 'administration/income_details.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'income_dets' : income_dets
	}
	
	return render(request, template_name, context)


@login_required
def expenses(request):
	user = request.user
	username = user.username
	template_name = 'administration/expenses.html'
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	expense = SchoolExpenses.objects.all().order_by('-date')

	if request.method == 'POST':
		year = request.POST['year']
		term = request.POST['term']
		title = request.POST['title']
		body = request.POST['body']

		expense = SchoolExpenses(
			year = year,
			term = term,
			name = title,
			content = body,
			)
		expense.save()
		return redirect('/administration/expense', {'info' : 'message sent successfuly'})

	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'expense' : expense
	}
	
	return render(request, template_name, context)


@login_required
def expenses_details(request, id):
	user = request.user
	username = user.username
	query = AdministrationProfile.objects.all().filter(admin_id = username)
	expense_dets = get_object_or_404(SchoolIncome, id=id)

	template_name = 'administration/income_details.html'
	context = {
	    'admin_profile' : query,
	    'admin_id': username,
	    'expense_dets' : expense_dets
	}
	
	return render(request, template_name, context)