from django.contrib import admin

from .models import Song, Users, Genre

class SongAdmin(admin.ModelAdmin):

    class Media:
        js = ('js/django-music/admin.js',)

admin.site.register(Song, SongAdmin)
admin.site.register(Genre)
admin.site.register(Users)