from django.db import models

# Create your models here.

class Phonebook(models.Model):  
    genre_name = models.CharField(max_length=50)
    genre_type = models.CharField(max_length=50)

    notes = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.genre_name)

    class Meta:
        ordering = ['genre_name']
