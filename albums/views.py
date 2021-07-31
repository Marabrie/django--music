from django.db.models.query import prefetch_related_objects
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Album, Artist
from .forms import AlbumForm, AlbumArtistForm
from django.shortcuts import redirect
#from django.http import HttpResponse

def album_create_views(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form': form
    }
    return render(request, "albums/album_create_views.html", context)

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'albums/album_create.html', {'form': form})

def album_edit(request, pk):
    album= get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
           album = form.save()
           return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form})

def album_delete(request,pk):
    album_to_delete = get_object_or_404(Album, pk=pk)
    album_to_delete.delete
    return redirect('album_list')
 
def artist_page(request, pk):
    artist= get_object_or_404(Artist, pk=pk)
    return render(request, 'albums/artist_page.html', {'artist': artist})  

def create_artist(request):
    if request.method == "GET":
        form = AlbumArtistForm()
        return render(request, 'albums/create_artist.html', {'form':form})
    elif request.method == "POST":
        form = AlbumArtistForm(request.POST)
        if form.is_valid():
            title = form.data['title']
            artist = form.data['artist']
            year = form.data['year']
            favorite = form.date['favorite']
            validated_artist = Artist.objects.get_or_create(artist=artist)[0]
            album = Album.objects.create(artist=validated_artist, title=title, year=year)
            album.save()
            return redirect('album_list', pk=album.pk)

def album_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.favorite = True
    album.save()
    return redirect('album_detail', pk=album.pk)


