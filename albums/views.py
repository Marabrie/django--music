from django.db.models.query import prefetch_related_objects
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Album
from .forms import AlbumForm
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
            album = form.save(commit=False)
            album.artist = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
        else:
            form = AlbumForm()
        return redirect(request, 'albums/album_edit.html', {'form': form})

def album_edit(request, pk):
    album= get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
           album = form.save(commit=False)
           album.author = request.user
           album_new.published_date = timezone.now()
           album_edit.save()
           return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form})

    def album_delete(request,pk):
        album_to_delete = get_object_or_404(Album, pk=pk)
        album_to_delete.delete
        return redirect('album_list')
    