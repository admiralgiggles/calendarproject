from django.contrib import admin
from .models import Camera, Rezervare

admin.site.register(Camera)
admin.site.register(Rezervare)

admin.site.site_title = 'Administrare calendar'
admin.site.index_title = 'Index'
admin.site.site_header = 'Administrare calendar'

admin.site.login_template = "calendar/login.html"