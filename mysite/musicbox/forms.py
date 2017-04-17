from django.forms import ModelForm, CharField, Form, PasswordInput
from django.db import models
from django import forms

from musicbox.models import Song, Users


class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = ('title', 'artist', 'genre', 'year', 'publisher', 'file')
	
	


class UsersForm(ModelForm):
	password = CharField(widget=PasswordInput())
	repassword = CharField(widget=PasswordInput())
	class Meta:
		model = Users

		fields = ('name_first', 'name_last','password','repassword', 'email', 'phone_number')


	def clean_repassword(self):
		password = self.cleaned_data.get('password')
		repassword = self.cleaned_data.get('repassword')
		if not repassword:
			raise forms.ValidationError("You must confirm your password")
		if password != repassword:
			raise forms.ValidationError("Your passwords do not match")
	 	return repassword


class SigninForm(ModelForm):
	password=CharField(widget=PasswordInput())
	class Meta:
		model = Users

		fields = ('email','password')
	def check(self):
		if not email:
			raise forms.ValidationError("You must provide you email address")
		if not pasword:
			raise forms.ValidationError("You must provide you passwords")

class RatingForm(forms.ModelForm):
	rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=[(5, "5"), (4, "4"), (3, "3"), (2, "2"), (1, "1")])

	class Meta:
		model = Song
		fields = ('rating',)
