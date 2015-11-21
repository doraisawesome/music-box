from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    
    
    
    def __unicode__(self):
        return '%s ' % (self.username)
    
    

