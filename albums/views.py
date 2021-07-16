from django.shortcuts import render
from django.utils import timezone
from .models import Albums

def albums_list(request):
    albums = Albums.objects.filter(created_at=timezone.now()).order_by('created_at')
    return render(request, 'albums/albums_list.html', {'albums': albums})

