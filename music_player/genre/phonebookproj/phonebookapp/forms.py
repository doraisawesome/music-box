from django import forms
from phonebookapp.models import Phonebook

class PhonebookForm(forms.ModelForm):

    genre_name = forms.CharField(min_length=3, max_length=50)


    class Meta:
        model = Phonebook 
