from django import forms
from .models import Albums
from django.db.models.fields import CharField


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = [
            'title',
            'artist',
            'Year_Released',
        ]