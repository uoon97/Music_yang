from django.shortcuts import render, redirect

from music.forms import MusicForm
from music.models import Music


def home(request):
    return render(request, 'home.html')

def author(request):
    return render(request, 'author.html')

def list_music(request):
    musics = Music.objects.all()
    return render(request, 'list_musics.html', {'musics': musics})

def update_music(request, id):
    music = Music.objects.get(id = id)
    form = MusicForm(request.POST or None, instance = music)

    if form.is_valid():
        form.save()
        return redirect('list_musics')

    return render(request, 'music_form.html', {'form': form, 'music': music})

def create_music(request):
    form = MusicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_musics')
    return render(request, 'music_form.html', {'form': form})

def delete_music(request, id):
    music = Music.objects.get(id=id)
    if request.method == 'POST':
        music.delete()
        return redirect('list_musics')

    return render(request, 'music_delete_confirm.html', {'music': music})

def search_basic(request):
    if 'q' in request.GET:
        q = request.GET['q']
        message = 'You searched for: %r' % request.GET['q']
        musics = Music.objects.filter(music_price__icontains=q)

    else:
        message = 'You submitted an empty form'
    return render(request, 'list_musics.html', {'message': message, 'musics': musics})

