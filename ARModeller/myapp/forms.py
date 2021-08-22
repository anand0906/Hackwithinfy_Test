from django.forms import ModelForm
from .models import *

class PizzaForm(ModelForm):
    class Meta:
        model=RecievingFromApp
        fields="__all__"