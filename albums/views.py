from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Album
from .forms import AlbumForm
from django.shortcuts import redirect

def album_create_views(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form': form
    }
    return render(request, "albums/album_create_views.html", context)

def album_list(request):
    albums = Album.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'albums': albums})

# def album_edit(request, pk):