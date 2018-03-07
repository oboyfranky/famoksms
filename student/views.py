from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StudentProfile
from django.contrib.auth.models import User
from sms_main.models import Messages, NoticeInfo, StudentFinance
from results.models import AcademicYear, StudentsRecord

# Create your views here.
@login_required
def dashboard(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	user_messages = Messages.objects.all().filter(reciever_id = username).order_by('-sent')[:2]
	user_notice = NoticeInfo.objects.all().filter(audience = 'Students').order_by('-submitted')[:1]
	template_name = 'students/dashboard.html'
	context = {
	    'std_profile' : query,
	    'stud_id': username,
	    'user_messages' : user_messages,
	    'user_notice' : user_notice
	}
	
	return render(request, template_name, context)

@login_required
def profile(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	template_name = 'students/profile.html'
	context = {
	    'std_profile' : query,
	    'stud_id': username
	}
	
	return render(request, template_name, context)

@login_required
def results(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	result = StudentsRecord.objects.all().filter(student = query).order_by('-marksheet')[:1]
	template_name = 'students/results.html'
	context = {
	    'std_profile' : query,
	    'stud_id': username,
	    'result' : result
	}
	
	return render(request, template_name, context)


@login_required
def results_details(request, id):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	results_det = get_object_or_404(StudentsRecord, id=id)

	template_name = 'students/results_details.html'
	context = {
	    'std_profile' : query,
	    'results_det' : results_det,
	    'stud_id': username
	}
	return render(request, template_name, context)


@login_required
def results_all(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	result = StudentsRecord.objects.all().filter(student = query).order_by('-marksheet')
	template_name = 'students/results_all.html'
	context = {
	    'std_profile' : query,
	    'stud_id': username,
	    'result' : result
	}
	
	return render(request, template_name, context)


@login_required
def messages(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
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
		return redirect('/student/send', {'info' : 'message sent successfuly'})
		#reverse_lazy('send')

	template_name = 'students/messages.html'
	context = {
	    'std_profile' : query,
	    'user_messages' : user_messages,
	    'stud_id': username
	}
	return render(request, template_name, context)

@login_required
def messages_details(request, id):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	message_det = get_object_or_404(Messages, id=id)

	template_name = 'students/messages_details.html'
	context = {
	    'std_profile' : query,
	    'message_det' : message_det,
	    'stud_id': username
	}
	return render(request, template_name, context)


@login_required
def send(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	user_sent = Messages.objects.all().filter(sender_id = username).order_by('-sent')

	template_name = 'students/sent.html'
	context = {
	    'std_profile' : query,
	    'user_sent' : user_sent,
	    'stud_id': username
	}
	return render(request, template_name, context)

@login_required
def send_details(request, id):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	sent_det = get_object_or_404(Messages, id=id)

	template_name = 'students/sent_details.html'
	context = {
	    'std_profile' : query,
	    'sent_det' : sent_det,
	    'stud_id': username
	}
	return render(request, template_name, context)

@login_required
def finance(request):
	user = request.user
	username = user.username
	template_name = 'students/finance.html'
	query = StudentProfile.objects.all().filter(stud_id = username)
	finance = StudentFinance.objects.all().filter(student = query).order_by('-year', '-term')[:1]
	status = StudentFinance.objects.all().filter(status = 'Paid')

	error = ''
	success = ''

	if status:
		success = 'Fees Successfuly Paid ' 
	else:
		error = 'Please be informed to pay full fees to participate in the examination'

	context = {
	    'std_profile' : query,
	    'stud_id': username,
	    'finance' : finance,
	    'error' : error,
	    'success' : success
	}
	
	return render(request, template_name, context)

@login_required
def finance_all(request):
	user = request.user
	username = user.username
	query = StudentProfile.objects.all().filter(stud_id = username)
	finance = StudentFinance.objects.all().filter(student = query).order_by('-year')
	template_name = 'students/finance_all.html'
	context = {
	    'std_profile' : query,
	    'stud_id': username,
	    'finance' : finance
	}
	
	return render(request, template_name, context)