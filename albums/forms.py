from django import forms
from .models import Album
from django.db.models.fields import CharField


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'Year_Released',
        ]