from django import forms  
from adminpanel.models import Loanagent
class loanForm(forms.ModelForm):  
    class Meta:  
        model = Loanagent
        fields = ['name','interest_pl','interest_bl','interest_hl','interest_el','interest_vl','principal_pl','principal_bl','principal_hl','principal_el','principal_vl','time_pl','time_bl','time_hl','time_el','time_vl'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
        'interest_pl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'interest_bl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'interest_hl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'interest_el': forms.TextInput(attrs={ 'class': 'form-control' }),
        'interest_vl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'principal_pl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'principal_bl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'principal_hl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'principal_el': forms.TextInput(attrs={ 'class': 'form-control' }),
        'principal_vl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'time_pl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'time_bl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'time_hl': forms.TextInput(attrs={ 'class': 'form-control' }),
        'time_el': forms.TextInput(attrs={ 'class': 'form-control' }),
        'time_vl': forms.TextInput(attrs={ 'class': 'form-control' }),
      }
        

        