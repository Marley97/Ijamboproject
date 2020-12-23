from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
	pro=Profil.objects.get(user=request.user)
	return render(request, 'simple_user.html', locals())

@login_required(login_url='login')	
def music(request):
	usr=request.user
	musique_form = MusicForm(request.POST or None,request.FILES)
	if(request.method=='POST'):
		if(musique_form.is_valid()):
			hh = musique_form.save(commit=False)
			hh.author = usr
			hh.save()
			return redirect('listeM')
	musique_form = MusicForm()
	return render(request,"forms.html",locals())

@login_required(login_url='login')
def musicalbum(request):
	usr=request.user
	musiquealbum_form = AlbumForm(request.user,request.POST or None,request.FILES)
	if(request.method=='POST'):
		if(musiquealbum_form.is_valid()):
			bb = musiquealbum_form.save(commit=False)
			bb.author=usr
			bb.save()
	musiquealbum_form = AlbumForm(request.user)
	return render(request,"forms.html",locals())

def songmonth(request):
	musiquemois_form = MonthSongForms(request.POST or None,request.FILES)
	if(request.method=='POST'):
		if(musiquemois_form.is_valid()):
			musiquemois_form.save()
	musiquemois_form = MonthSongForms()
	return render(request,"forms.html",locals())

def ListMusic(request):
	musics = Music.objects.filter(author=request.user)
	return render(request, "listes.html", locals())

@login_required(login_url='login')
def EventRegester(request):
	InputEvent = EventForm(request.POST or None, request.FILES)
	if(request.method == 'POST'):
		if(InputEvent.is_valid()):
			cc = InputEvent.save(commit = False)
			cc.author = request.user
			cc.save()
	InputEvent = EventForm()
	return render(request, "forms.html", locals())




