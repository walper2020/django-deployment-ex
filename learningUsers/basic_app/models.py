from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #creat relationship(dont inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #adittional attributes for User
    portfolio_site = models.URLField(blank = True)   #user doesnt have to fill this
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    #-----------------
    def __str__(self):
        #built-in attr of django.contrib.auth.models.User  for printing this out
        return self.user.username
