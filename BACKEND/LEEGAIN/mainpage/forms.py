from django import forms
from .models import Info
from django.forms import modelformset_factory

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'content', 'image']