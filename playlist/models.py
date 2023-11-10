from django.db import models


class UserPlayList(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    videos_qty = models.IntegerField(default=0)
    views_qty = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
# class Video(models.Model):
#     url = models.URLField()
#     views = models.IntegerField()
#     model = models.CharField(max_length=55)

#     def __str__(self):
#         return f"{self.url} - {self.views} views - {self.model}"

class Video(models.Model):
       title = models.CharField(max_length=100)
       url = models.URLField()
       description = models.TextField()

       def __str__(self):
        return self.name