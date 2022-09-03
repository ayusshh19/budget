from django import forms
import datetime
from datetime import datetime as ti

from .models import add_spends
now = ti.now()
current_time = now.strftime("%H:%M:%S")
date_time = datetime.datetime.now()
print(date_time)


class spend_form(forms.ModelForm):
    spend_CHOICES = (
    ("spend", "spend"),
    ("get", "get"),
)
    reason=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    amount=forms.CharField(max_length=100,widget=forms.NumberInput(attrs={'class':'form-control'}))

    
    class Meta:
        model =add_spends
        fields = ['reason','amount','type'] # list of fields you want from model
    
    