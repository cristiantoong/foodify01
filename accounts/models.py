from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.shortcuts import redirect, reverse
from django.db.models.signals import post_save

class UserProfile(models.Model):
    profile_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)   
    profile_pic = models.ImageField(null=True, blank=True)
    cover_photo = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.profile_name)

    

# associating the user has been created with the user profile
# def create_profile(sender, **kwargs):
#     # if user object has been created
#     if kwargs['created']:
#         # create user profile                      #current user
#         user_profile = UserProfile.objects.create(profile_name=kwargs['instance']) 

# post_save.connect(create_profile, sender=User)

