from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Albums
from .forms import AlbumForm
from django.shortcuts import redirect

def albums_create_views(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form': form
    }
    return render(request, "albums/albums_create_views.html", context)

def albums_list(request):
    albums = Albums.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'albums/albums_list.html', {'albums': albums})

def albums_detail(request, pk):
    albums = get_object_or_404(Albums, pk=pk)
    return render(request, 'albums/albums_detail.html', {'albums': albums})

# def albums_edit(request, pk):