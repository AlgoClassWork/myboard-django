from django.db import models

# Create your models here.
class Ad(models.Model):
    image = models.ImageField(upload_to='ad_images/')
    description = models.TextField()
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title