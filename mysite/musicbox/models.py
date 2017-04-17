import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from utils import get_file_upload_path, get_cover_upload_path
from django.core.files.storage import FileSystemStorage

from django.core.validators import RegexValidator
# from __future__ import unicode_literals

from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate, get_user_model
#import eyed3 # needed installation


class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    #genre_type = models.CharField(max_length=50)

    #notes = models.TextField()
    #creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return (self.genre_name)

    #class Meta:
     #  ordering = ['genre_name',]

# model for song info(code retrieved from https://github.com/muratcorlu/django-music)
class Song(models.Model):
    #file = models.FileField(_('File'), upload_to=get_file_upload_path)
    title = models.CharField(_('Title'), max_length=100)
    artist = models.CharField(_('Artist'), max_length=100)
    #genre = models.CharField(_('Genre'), max_length=50)
    genre = models.ForeignKey(Genre, null=True)
	
    year = models.CharField(_('Year'), max_length=4, blank=True)
    publisher = models.CharField(_('Publisher'), max_length=100, blank=True)
    rating = models.IntegerField(_('Rating'),default=0)
    overall_rating = models.IntegerField(_('Overall Rating'),default=0)
    #cover_image = models.ImageField(_('Cover image'), upload_to=get_cover_upload_path, blank=True)
    total_rating = models.IntegerField(_('Total Rating'), default=0)
    sumitted_count = models.IntegerField(_('Total Rating Submmited'), default=0)

    play_count = models.IntegerField(_('Play count'), default=0)

    added_date = models.DateTimeField(auto_now_add=True)

    file = models.FileField(upload_to='music', null=True)

    def filename(self):
		return os.path.basename(self.file.name)

    def save(self, *args, **kwargs):
        self.file_size = self.file.size

        super(Song, self).save(*args, **kwargs)

        file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)

        '''
        if eyeD3.isMp3File(file_path):
            audioFile = eyeD3.Mp3AudioFile(file_path)
            self.duration = audioFile.getPlayTime()

            tag = audioFile.getTag()
            self.artist = tag.getArtist()
            self.album = tag.getAlbum()
            self.track_number = tag.getTrackNum()
        '''

        super(Song, self).save(*args, **kwargs)


    def __unicode__(self):
        return "%s" % self.title

class Choice(models.Model):
    rateValue = models.ForeignKey(Song, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Music(models.Model):
	file = models.FileField(upload_to='music', null=True, blank = True)
	title = models.CharField(max_length=15)
	genre = models.CharField(max_length=15)
	artist = models.CharField(max_length=15)

	def filename(self):
		return os.path.basename(self.file.name)


# model for user info
class Users(models.Model):
    name_first = models.CharField(max_length=10)
    name_last = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    repassword = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^1?\D*(\d{3})\D*(\d{3})\D*(\d{4})$', message="phone number must be in the format XXX-XXX-XXXX")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True) #validators should be a list


    def __unicode__(self):
        return (self.name_first + " " + self.name_last)
