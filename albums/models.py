from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.fields.related import ForeignKey


class Artist(models.Model):
    artist = models.CharField(max_length=200)
    
    def __str__(self):
        return self.artist
    
    class Meta:
        ordering = ['artist']


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    Year_Released = models.IntegerField(blank=True, null=True)
    favorite = models.BooleanField(default=False)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        