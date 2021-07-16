from django.shortcuts import render

def albums_list(request):
    return render(request, 'albums/albums_list.html', {})

