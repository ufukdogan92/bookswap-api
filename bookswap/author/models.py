#! -*- coding:utf-8 -*-
from django.db import models 
import datetime
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.TextField(max_length=50)
    birthdate = models.DateField(blank=True, null=True,default=datetime.date.today)

    def __str__(self):
        return self.first_name+" "+self.last_name
    class Meta:
        verbose_name ="Yazar"
        verbose_name_plural="Yazarlar"

