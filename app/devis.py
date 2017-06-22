from django import forms
from models import *

class Create_estimate(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
