from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    user_bio = models.TextField(blank=True,max_length=100)
    user_profile_img = models.ImageField(upload_to='profile_images', default='default_user.png')


    def __str__(self):
        return self.user.get_username