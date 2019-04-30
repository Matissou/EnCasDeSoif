from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    pseudo = models.CharField(max_length=100, default="")
    age = models.IntegerField(default=18)   

    def __str__(self):
        return self.pseudo

def create_profile(sender,**kwargs):
    # If this user has been created
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)