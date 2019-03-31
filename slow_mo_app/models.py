from django.db import models

# Create your models here.
class uploadedVideo(models.Model):
    name = models.CharField(max_length=500)
    video = models.FileField(upload_to='inputVid/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name + ": " + str(self.video)
