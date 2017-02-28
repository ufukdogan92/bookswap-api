#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
from bookswap.author.models import Author
# Create your models here.



class Offer(models.Model):
    owner = models.ForeignKey(User,unique=False)
    author = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=50)
    Latitude  = models.DecimalField(max_digits=20,decimal_places=10,blank=True, null=True)
    Longitude = models.DecimalField(max_digits=20,decimal_places=10,blank=True, null=True)
    descr = models.TextField(max_length=220,blank=True, null=True)
    image = models.ImageField(upload_to="books",blank=True, null=True)
    is_active = models.BooleanField(default=True)
    bidders = models.ManyToManyField(User, db_table='bidders', related_name='offer_users', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name ="İlan"
        verbose_name_plural="İlanlar"

