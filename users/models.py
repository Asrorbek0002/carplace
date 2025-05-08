from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


"""
1. Default User Modelini extend qilish
class CustomUser(User): 
     avatar = ...

2. AbstractUser Modelni extend qilish  >>>  Ko'p preyktlar shu bilan ishlaydi
     avatar = ...
   
3. AbstractBaseUser Modelni extend qilish
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = 
    avatar =    
  
4. Alohida Profil modelni ochib , Default userga One2One qilish
class Profile(model.Model):
    user = models.One2OneField(CustomUser, on_delete=model.CASCADE)
"""
