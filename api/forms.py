# forms.py - Andy Alexa @2017

from django.forms import ModelForm, DateInput, TextInput, Select, Textarea, HiddenInput
from api.models import Rezervare, Camera

class RezervareForm(ModelForm):
    class Meta:
        model = Rezervare
        fields = '__all__'
        widgets = {
            'nume': TextInput(attrs={
                'class': 'form-control'
            }),
            'prenume': TextInput(attrs={
                'class': 'form-control'
            }),
            'serie_buletin': TextInput(attrs={
                'class': 'form-control'
            }),
            'adresa': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'class': 'form-control'
            }),
            'telefon': TextInput(attrs={
                'class': 'form-control'
            }),
            'tara': TextInput(attrs={
                'class': 'form-control'
            }),
            'localitate': TextInput(attrs={
                'class': 'form-control'
            }),
            'date_start': DateInput(attrs={
                'id': 'dateStartPicker',
                'class': 'form-control'
            }), 
            'date_end': DateInput(attrs={
                'id': 'dateEndPicker',
                'class': 'form-control',
            }),
            'camera': Select(attrs={
                'class': 'form-control'
            }),
            'comentariu': Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            })
        }

class CameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'
        widgets = {
            'numar': TextInput(attrs={
                'class': 'form-control'
            })
        }
