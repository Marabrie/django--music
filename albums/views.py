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
    album = Album.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'albums/album_list.html', {'album': album})

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
        return render(request, 'albums/album_edit.html', {'form': form})

def album_edit(request, pk):
    post = get_object_or_404(album_create_views, pk=pk)
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
