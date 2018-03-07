from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^dashboard/$', dashboard, name = 'dashboard'),
	url(r'^profile/$', profile, name = 'profile'),
	url(r'^messages/$', messages, name = 'messages'),
	url(r'^messages/(?P<id>\d+)/$', messages_details, name = 'messages_details'),
	url(r'^send/$', send, name = 'send'),
	url(r'^send/(?P<id>\d+)/$', send_details, name = 'send_details'),
	url(r'^notice/$', notice, name = 'notice'),
	url(r'^notice/(?P<id>\d+)/$', notice_details, name = 'notice_details'),
	url(r'^finance/$', finance, name = 'finance'),

	url(r'^income/$', income, name = 'income'),
	url(r'^income/(?P<id>\d+)/$', income_details, name = 'income_details'),

	url(r'^expenses/$', expenses, name = 'expenses'),
	url(r'^expenses/(?P<id>\d+)/$', expenses_details, name = 'expenses_details'),

	url(r'^students_profile/$', stud_profile, name = 'stud_profile'),
	url(r'^students_profile/(?P<id>\d+)/$', stud_profile_details, name = 'stud_profile_details'),

	url(r'^parents/$', parents, name = 'parents'),
	url(r'^parents/(?P<id>\d+)/$', par_profile_details, name = 'par_profile_details'),

	url(r'^teachers/$', teachers, name = 'teachers'),
	url(r'^teachers/(?P<id>\d+)/$', tea_profile_details, name = 'tea_profile_details'),
	
	# url(r'^results/$', results, name = 'results')
]