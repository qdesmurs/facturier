# -*- coding: utf-8 -*-
from django.forms import inlineformset_factory

from .models import *

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

LineFormSet = inlineformset_factory(Project, Project_line, fields=['name', 'quantity', 'unit_price'] , extra=1)
