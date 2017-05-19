#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
import datetime
from django.db.models.signals import post_save


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = UserProfile(user=user)
        up.save()
post_save.connect(create_profile, sender=User, dispatch_uid="users-profilecreation-signal")

class UserProfile(models.Model):
    user = models.ForeignKey(User,related_name="userprofile")

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True,default=datetime.date.today)
    phone = models.CharField(max_length=12,blank=True, null=True)
    image = models.ImageField(blank=True, null=True,upload_to="users/")
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name ="Kullanıcı Profili"
        verbose_name_plural="Kullanıcı Profilleri"