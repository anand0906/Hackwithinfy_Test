from django.forms import ModelForm
from .models import *

class InputForm(ModelForm):
    class Meta:
        model=RecievingFromApp
        fields="__all__"