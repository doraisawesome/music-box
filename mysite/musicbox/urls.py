from django.conf.urls import url

<<<<<<< HEAD
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^genre/$', views.genre, name='genre'),
	url(r'^about/$', views.about, name='about'),
	url(r'^upload/$', views.upload, name='upload'),
	
	# Need change this later. Originally made by Fan.
	url(r'^$', 'musicbox.views.genre', name="contact-list"),
    url(r'^(?P<contact_id>\d+)/$',
         'musicbox.views.contact_detail', name='contact-detail'),
    url(r'^create/$',
         'musicbox.views.create_contact', name="create-contact"),
    url(r'^edit/(?P<contact_id>\d+)/$', 
         'musicbox.views.edit_contact', name='edit-contact'),
    url(r'^delete/(?P<contact_id>\d+)/$',
        'musicbox.views.delete_contact', name='delete-contact'), 
	
	#url(r'^(?P<contact_id>[0-9]+)/$', 'contact_manager.views.detail', name="detail"),
] 
=======
from . import views
>>>>>>> 4156a491604122356ac49354964973d60747688b
