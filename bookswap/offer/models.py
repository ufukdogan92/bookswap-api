#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
from bookswap.author.models import Author
# Create your models here.



class Offer(models.Model):
    owner = models.ForeignKey(User,unique=False)
    author = models.ForeignKey(Author,unique=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=50)
    Latitude  = models.DecimalField(max_digits=20,decimal_places=10)
    Longitude = models.DecimalField(max_digits=20,decimal_places=10)
    descr = models.TextField(max_length=220)
    image = models.ImageField(upload_to="books")
    is_active = models.BooleanField(default=True)
    bidders = models.ManyToManyField(User, db_table='bidders', related_name='offer_users', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name ="İlan"
        verbose_name_plural="İlanlar"

