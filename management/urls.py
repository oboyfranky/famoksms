from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('accounts.urls')),
	url(r'^student/', include('student.urls', namespace='student')),
	url(r'^teacher/', include('teacher.urls', namespace='teacher')),
	url(r'^parent/', include('parent.urls', namespace='parent')),
	url(r'^administration/', include('administration.urls', namespace='administration')),
	url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)