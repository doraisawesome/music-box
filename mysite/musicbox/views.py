from django.shortcuts import render

<<<<<<< HEAD
from .models import Music

def index(request):
	return render(request,'musicbox/index.html')

def home(request):
	return render(request,'musicbox/home.html')

def signup(request):
	return render(request,'musicbox/signup.html')
	
def about(request):
	return render(request,'musicbox/about.html')
	
#def genre(request):
#	return render(request,'musicbox/genre.html')
	
def upload(request):
	return render(request,'musicbox/upload.html')
	
	
# Need to change the namings, etc. of the following many lines of code. Made by Fan originally.
from django.shortcuts import get_object_or_404, render, redirect
from musicbox.models import Phonebook
from musicbox.forms import PhonebookForm


def genre(request):
    contacts = Phonebook.objects.all()
    return render(request, 'musicbox/genre.html')

def contact_detail(request, contact_id):
    contact = get_object_or_404(Phonebook, pk=contact_id)
    return render(request, 'musicbox/contact_detail.html', {'contact': contact})

def create_contact(request):
    if request.method == 'POST':
        form = PhonebookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
    else:
        form = PhonebookForm()
    return render(request, 'musicbox/create_contact.html', {'form': form})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Phonebook, pk=contact_id)
    if request.method == 'POST':
        form = PhonebookForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact-detail', contact_id)
    else:
        form = PhonebookForm(instance=contact)
    return render(request, 'musicbox/edit_contact.html', {'form': form})

    
def delete_contact(request, contact_id):
    contact = get_object_or_404(Phonebook, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('/musicbox/')
    return render(request, 'musicbox/delete_contact.html', {'contact': contact})
=======
# Create your views here.
from .models import Song

def home(request):
	recommand_list = Song.objects.all()  # later will change the list according to rating
	return render(request,'musicbox/home.html',{'recommand_list':recommand_list})
>>>>>>> 4156a491604122356ac49354964973d60747688b
