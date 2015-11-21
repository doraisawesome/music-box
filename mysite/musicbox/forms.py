from django.forms import ModelForm
#from django import forms

# Need to change the following code. Orininally made by Fan.
from musicbox.models import Phonebook

class PhonebookForm(ModelForm):
    class Meta:
		model=Phonebook
		fields = ('genre_name',)