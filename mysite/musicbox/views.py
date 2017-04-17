from django.shortcuts import render, get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import fields
from django.contrib import messages

from musicbox.models import Users, Music, Song, Genre
from musicbox.forms import UsersForm, SigninForm, SongForm, RatingForm

def home(request):
    recommand_list = Song.objects.filter(rating__gte=3)  
    new_list = Song.objects.filter(play_count=0)
    return render(request,'musicbox/home.html', {
        'new_list':new_list,
        'recommand_list': recommand_list
        })

def index(request):
	return render(request,'musicbox/index.html')

def signup(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign up successful!')
            return redirect(reverse('musicbox:signin'))
    else:
        form = UsersForm()

    return render(request,'musicbox/signup.html',{'form': form})
	
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            useremail = request.POST['email']
            userpassword = request.POST['password']
            try:
                targetuser = Users.objects.filter(email = useremail)
                try:
                    user = Users.objects.get(email = useremail, password = userpassword)
                    messages.success(request, 'Welcome ' + user.name_first + " " + user.name_last + " !")
                    return redirect(reverse('musicbox:home'))
                except:
                    messages.error(request, 'Error: Invalid pasword!')
                    return redirect(reverse('musicbox:signin'))
            except Users.DoesNotExist:
                messages.error(request, 'Error: Invalid email!')
                return redirect(reverse('musicbox:signin'))


            # return redirect(reverse('musicbox:index'))
    else:
        form = SigninForm()

        # userlist = Users.objects.order_by('name_last')
    return render(request,'musicbox/signin.html',{'form': form})
        # return redirect(reverse('musicbox:home'))

def ratingList(request):
    recommand_list = Song.objects.all()
    rated_list = Song.objects.exclude(overall_rating=0)#[:10]
    no_rating = Song.objects.filter(overall_rating=0)

    return render(request,'musicbox/rating.html', {
        'rated_list': rated_list,
        'no_rating':no_rating,
        'recommand_list': recommand_list,
        })

def songDetails(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = RatingForm(request.POST or None, instance=song)
        oldrate = song.overall_rating
        if form.is_valid():
            song.sumitted_count += 1
            form.save()
            song.total_rating = song.rating+song.total_rating
            song.overall_rating = song.total_rating//song.sumitted_count
            form.save()
            return redirect(reverse('musicbox:songDetails', args=(song_id)))
    else:
        form = RatingForm(instance=song)
        song.play_count +=1
        song.save()
    return render(request, 'musicbox/songDetails.html', {
        'songdetails': song,
        'form': form
        })

def about(request):
	return render(request,'musicbox/about.html')

def upload(request):
	if request.method == 'POST':
		form = SongForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Upload successful!')
			return redirect(reverse('musicbox:upload'))
	else:
		form = SongForm()
	return render(request, 'musicbox/upload.html', {'form': form})


def genre(request):
    genre_list = Genre.objects.all()
    return render(request, 'musicbox/genre.html', {'genre_list':genre_list})

def songsofgenre(request, genre_id):
    songsofgenre_list = Song.objects.filter(genre__pk=genre_id)
    genre = Genre.objects.get(pk=genre_id)
    genre_list = Genre.objects.all()
    #songsofgenre_list = Song.objects.filter(genre=genre_id)
    return render(request, 'musicbox/songsofgenre.html', {
        'songsofgenre_list': songsofgenre_list,
        'genre': genre,
        'genre_list': genre_list
        })


def billboard(request):
    chart = billboard.ChartData('hot-100')

    return render(request, 'musicbox/home.html',{'chart': chart})

