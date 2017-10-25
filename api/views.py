# views.py - Andy Alexa @2017

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader

# app imports
from .models import *
from .calendar import *
from .forms import *
import logging

logger = logging.getLogger(__name__)

# render calendar
def calendar(request):
    
    all_rezervations = Rezervare.objects.all()
    rezervations_count = Rezervare.objects.all().count

    all_cameras = Camera.objects.all()
    get_camera_number = Rezervare.objects.only('camera')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        rezervation_arr = []
        if request.GET.get('camera') == "all":
            all_rezervations = Rezervare.objects.all()
        else:   
            all_rezervations = Rezervare.objects.filter(camera__numar__icontains=request.GET.get('camera'))

    # register forms 
    add_rezervation_form = RezervareForm()
    add_camera_form = CameraForm()

    context = {
        "cameras": all_cameras,
        "rezervations": all_rezervations,
        "rezervations_count": rezervations_count,
        "get_camera_number": get_camera_number,
        "form": add_rezervation_form,
        "form1": add_camera_form
    }

    return render(request, 'calendar/index.html', context)

# add new rezervation or update existing
def add_rezervation(request):
    if request.POST:
        form = RezervareForm(request.POST)
        if form.is_valid():
            param = request.POST['camera']
            received_param = request.POST['sent_param']

            received_id = request.POST['rez_id']
            new_values = form.cleaned_data

            if received_id.isdigit():
                Rezervare.objects.filter(rez_id=received_id).update(
                    nume = new_values["nume"],
                    prenume = new_values["prenume"],
                    serie_buletin = new_values["serie_buletin"],
                    adresa = new_values["adresa"],
                    email = new_values["email"],
                    telefon = new_values["telefon"],
                    tara = new_values["tara"],
                    localitate = new_values["localitate"],
                    camera = new_values["camera"],
                    date_start = new_values["date_start"],
                    date_end = new_values["date_end"],
                    comentariu = new_values["comentariu"]
                )
                
            elif received_id == "none":
                form.save()

        if not received_param == "none":
            return HttpResponseRedirect('/?camera=' + param)
            
        else:
            return HttpResponseRedirect('/')
      
    else:
        messages.error(request, "Error")
        return render(request, 'calendar/index.html', context)


# update a rezervation drag and drop
def update_rezervation(request):
    if request.POST:
        rez = Rezervare.objects.get(rez_id = request.POST.get('rez_id'))
        rez.date_start = request.POST.get('date_start')
        rez.date_end = request.POST.get('date_end')
        
        rez.save()

    return HttpResponse('updated')

# delete rezervation
def delete_rezervation(request):
    if request.POST:
        obj = Rezervare.objects.get(rez_id = request.POST['rez_id'])
        obj.delete()

    return HttpResponse('deleted')

# add new camera
def add_camera(request):
    if request.POST:
        form1 = CameraForm(request.POST)
        if form1.is_valid():
            form1.save()

        return HttpResponseRedirect('/')