from django import forms
from .models import Album
from .models import Artist 
from django.db.models.fields import CharField


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'artist','Year_Released',)
        
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('artist',)

class AlbumArtistForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    artist = forms.CharField(max_length=50)
    year = forms.IntegerField()
    favorite = forms.BooleanField(required=False) 
     