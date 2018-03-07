from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ParentProfile
from student.models import StudentProfile
from django.contrib.auth.models import User
from sms_main.models import Messages, NoticeInfo, StudentFinance
from results.models import AcademicYear, StudentsRecord

# Create your views here.
@login_required
def dashboard(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	user_messages = Messages.objects.all().filter(reciever_id = username).order_by('-sent')[:2]
	user_notice = NoticeInfo.objects.all().filter(audience = 'Parents').order_by('-submitted')[:1]
	template_name = 'parents/dashboard.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'user_messages' : user_messages,
	    'user_notice' : user_notice
	}
	
	return render(request, template_name, context)

@login_required
def profile(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	ward = StudentProfile.objects.all().filter(parent = query)
	template_name = 'parents/profile.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'ward' : ward
	}
	
	return render(request, template_name, context)


@login_required
def messages(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
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
		return render(request, 'parents/messages.html', {'info' : 'message sent successfuly'})

	template_name = 'parents/messages.html'
	context = {
		'par_profile' : query,
	    'par_id': username,
	    'user_messages' : user_messages,
	}
	return render(request, template_name, context)

@login_required
def messages_details(request, id):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	message_det = get_object_or_404(Messages, id=id)

	template_name = 'parents/messages_details.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'message_det' : message_det,
	}
	return render(request, template_name, context)


@login_required
def send(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	user_sent = Messages.objects.all().filter(sender_id = username).order_by('-sent')

	template_name = 'parents/sent.html'
	context = {
	    'par_profile' : query,
	    'user_sent' : user_sent,
	    'par_id': username
	}
	return render(request, template_name, context)

@login_required
def send_details(request, id):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	sent_det = get_object_or_404(Messages, id=id)

	template_name = 'parents/sent_details.html'
	context = {
	    'par_profile' : query,
	    'sent_det' : sent_det,
	    'par_id': username
	}
	return render(request, template_name, context)


@login_required
def ward_profile(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	ward = StudentProfile.objects.all().filter(parent = query)
	template_name = 'parents/ward_profile.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'ward' : ward
	}
	
	return render(request, template_name, context)


@login_required
def results(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	ward = StudentProfile.objects.all().filter(parent = query)	
	result = StudentsRecord.objects.all().filter(student = ward).order_by('-marksheet')[:1]
	template_name = 'parents/results.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'result' : result
	}
	
	return render(request, template_name, context)


@login_required
def results_details(request, id):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	results_det = get_object_or_404(StudentsRecord, id=id)

	template_name = 'parents/results_details.html'
	context = {
	    'par_profile' : query,
	    'results_det' : results_det,
	    'par_id': username
	}
	return render(request, template_name, context)


@login_required
def results_all(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	ward = StudentProfile.objects.all().filter(parent = query)	
	result = StudentsRecord.objects.all().filter(student = ward).order_by('-marksheet')
	template_name = 'parents/results_all.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'result' : result
	}
	
	return render(request, template_name, context)


@login_required
def finance(request):
	user = request.user
	username = user.username
	template_name = 'parents/finance.html'
	query = ParentProfile.objects.all().filter(parent_id = username)
	ward = StudentProfile.objects.all().filter(parent = query)	
	finance = StudentFinance.objects.all().filter(student = ward).order_by('-year', '-term')[:1]
	status = StudentFinance.objects.all().filter(status = 'Paid')

	error = ''
	success = ''

	if status:
		success = 'Fees Successfuly Paid' 
	else:
		error = 'Please be informed to pay your ward\'s fees in full for them to participate in the examination'

	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'finance' : finance,
	    'error' : error,
	    'success' : success
	}
	
	return render(request, template_name, context)

@login_required
def finance_all(request):
	user = request.user
	username = user.username
	query = ParentProfile.objects.all().filter(parent_id = username)
	ward = StudentProfile.objects.all().filter(parent = query)	
	finance = StudentFinance.objects.all().filter(student = ward).order_by('-year')
	template_name = 'parents/finance_all.html'
	context = {
	    'par_profile' : query,
	    'par_id': username,
	    'finance' : finance
	}
	
	return render(request, template_name, context)