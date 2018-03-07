from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^dashboard/$', dashboard, name = 'dashboard'),
	url(r'^profile/$', profile, name = 'profile'),
	url(r'^results/$', results, name = 'results'),
	url(r'^results/(?P<id>\d+)/$', results_details, name = 'results_details'),
	url(r'^results_all/$', results_all, name = 'results_all'),
	url(r'^messages/$', messages, name = 'messages'),
	url(r'^messages/(?P<id>\d+)/$', messages_details, name = 'messages_details'),
	url(r'^send/$', send, name = 'send'),
	url(r'^send/(?P<id>\d+)/$', send_details, name = 'send_details'),
	url(r'^ward_profile/$', ward_profile, name = 'ward_profile'),
	url(r'^finance/$', finance, name = 'finance'),
	url(r'^finance_all/$', finance_all, name = 'finance_all')
]