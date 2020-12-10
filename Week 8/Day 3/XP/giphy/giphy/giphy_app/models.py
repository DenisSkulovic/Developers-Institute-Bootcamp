from django.db import models
import datetime



class Gif(models.Model):
    
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploader_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"GIF: {self.title}"
    
class Category(models.Model):
    
    name = models.CharField(max_length=255)
    gifs = models.ManyToManyField(to=Gif)