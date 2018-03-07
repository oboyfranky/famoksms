from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^dashboard/$', dashboard, name = 'dashboard'),
	url(r'^profile/$', profile, name = 'profile'),
	url(r'^messages/$', messages, name = 'messages'),
	url(r'^messages/(?P<id>\d+)/$', messages_details, name = 'messages_details'),
	url(r'^send/$', send, name = 'send'),
	url(r'^send/(?P<id>\d+)/$', send_details, name = 'send_details'),
	url(r'^students/$', students, name = 'students'),
	url(r'^students_profile/(?P<id>\d+)/$', stud_profile_details, name = 'stud_profile_details'),

]