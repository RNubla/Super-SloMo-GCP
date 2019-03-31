from django.db import models

# Create your models here.
class uploadedVideo(models.Model):
    vidName = models.CharField(max_length=100)
    vidDuration = models.TimeField()

class downloadVideo(models.Model):
    vidOutName = models.CharField(max_length=25)
    vidOutDuration = models.TextField()
