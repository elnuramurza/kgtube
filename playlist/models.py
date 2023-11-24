from django.db import models
from django.contrib.auth.models import User


class UserPlayList(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    videos_qty = models.IntegerField(default=0)
    views_qty = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название плейлиста")
    owner = models.ForeignKey(User, 
    on_delete=models.CASCADE,
    related_name="playlists",
    verbose_name="Владелец")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлисты"        