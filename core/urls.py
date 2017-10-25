from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', calendar, name='calendar'),
    url(r'^login/$', login, {'template_name': 'calendar/login.html'}),

    # camera methods
    url(r'^add_camera/', add_camera, name='add_camera'),

    # rezervation methods
    url(r'^add_rezervation/', add_rezervation, name='add_rezervation'),
    url(r'^update_rezervation/', update_rezervation, name='update_rezervation'),
    url(r'^delete_rezervation/', delete_rezervation, name='delete_rezervation'),
]