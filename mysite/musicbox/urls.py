from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^rating/$', views.ratingList, name='rating'), 
	url(r'^rating/(?P<song_id>\d+)/$', views.songDetails, name='songDetails'), 
	url(r'^home/(?P<song_id>\d+)/$', views.songDetails, name='songDetails'), 
	url(r'^genre/$', views.genre, name='genre'),
	url(r'^genre/(?P<genre_id>\d+)/$', views.songsofgenre, name='songsofgenre'),
	url(r'^about/$', views.about, name='about'),
	url(r'^upload/$', views.upload, name='upload'),
]
