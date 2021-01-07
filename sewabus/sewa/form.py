from django.forms import ModelForm
from django import forms
from .models import Sewa

  
class PesanForm(ModelForm): 
    class Meta: 
        model = Sewa
        fields = "__all__"

    # widgets = {
    #         'tanggal_mulai': AdminDateWidget()
    #     }

    # widgets ={
    #     'tanggal_mulai': 
        

    # }
