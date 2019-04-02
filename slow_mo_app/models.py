from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=500)
    videoFile = models.FileField(upload_to='videos/', null=True,verbose_name="")
    objects = models.Manager()
    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ": " + str(self.videoFile)
