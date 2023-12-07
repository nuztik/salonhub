from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from .models import Service


class ServiceForm(forms.ModelForm):
    # title = forms.CharField(max_length=200)

    class Meta:
        model = Service
        fields = [
            'title',
            'content',
            'price',
            'times'
        ]


