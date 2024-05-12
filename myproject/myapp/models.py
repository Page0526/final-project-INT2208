from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.TextField()
    profile_image = models.ImageField(upload_to='avatars/', blank=True) # save avatar
    
# model to save PDF history
class PDFHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pdf_histories')
    pdf = models.FileField(upload_to='', blank=True)
    image = models.ImageField(upload_to='', null=True, blank=True)

