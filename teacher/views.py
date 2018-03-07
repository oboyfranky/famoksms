from django.views.generic import *
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TeacherProfile
from django.contrib.auth.models import User
from student.models import StudentProfile
from sms_main.models import Messages, NoticeInfo
from results.models import AcademicYear, StudentsRecord

# Create your views here.
@login_required
def dashboard(request):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
	user_messages = Messages.objects.all().filter(reciever_id = username).order_by('-sent')[:2]
	user_notice = NoticeInfo.objects.all().filter(audience = 'Teachers').order_by('-submitted')[:1]
	template_name = 'teachers/dashboard.html'
	context = {
	    'tea_profile' : query,
	    'teach_id': username,
	    'user_messages' : user_messages,
	    'user_notice' : user_notice
	}
	
	return render(request, template_name, context)

@login_required
def profile(request):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
	template_name = 'teachers/profile.html'
	context = {
	    'tea_profile' : query,
	    'teach_id': username
	}
	
	return render(request, template_name, context)

@login_required
def students(request):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)

	form1 = StudentProfile.objects.all().filter(current_class = 'Form 1')
	form2 = StudentProfile.objects.all().filter(current_class = 'Form 2')
	form3 = StudentProfile.objects.all().filter(current_class = 'Form 3')

	template_name = 'teachers/students.html'
	context = {
	    'tea_profile' : query,
	    'teach_id': username,
	    'form1' : form1,
	    'form2' : form2,
	    'form3' : form3
	}
	
	return render(request, template_name, context)


@login_required
def stud_profile_details(request, id):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
	students_det = get_object_or_404(StudentProfile, id=id)
	template_name = 'teachers/stud_profile_details.html'
	context = {
	    'tea_profile' : query,
	    'teach_id': username,
	    'students_det' : students_det
	}
	
	return render(request, template_name, context)
	

@login_required
def messages(request):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
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
		return redirect('/teacher/send', {'info' : 'message sent successfuly'})
		#reverse_lazy('send')

	template_name = 'teachers/messages.html'
	context = {
	    'tea_profile' : query,
	    'user_messages' : user_messages,
	    'teach_id': username
	}
	return render(request, template_name, context)

@login_required
def messages_details(request, id):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
	message_det = get_object_or_404(Messages, id=id)

	template_name = 'teachers/messages_details.html'
	context = {
	    'tea_profile' : query,
	    'message_det' : message_det,
	    'teach_id': username
	}
	return render(request, template_name, context)


@login_required
def send(request):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
	user_sent = Messages.objects.all().filter(sender_id = username).order_by('-sent')

	template_name = 'teachers/sent.html'
	context = {
	    'tea_profile' : query,
	    'user_sent' : user_sent,
	    'teach_id': username
	}
	return render(request, template_name, context)

@login_required
def send_details(request, id):
	user = request.user
	username = user.username
	query = TeacherProfile.objects.all().filter(teach_id = username)
	sent_det = get_object_or_404(Messages, id=id)

	template_name = 'teachers/sent_details.html'
	context = {
	    'tea_profile' : query,
	    'sent_det' : sent_det,
	    'teach_id': username
	}
	return render(request, template_name, context)


