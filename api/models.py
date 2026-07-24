from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class CustomUser(AbstractUser):
    name=models.CharField(max_length=30, blank=False, null=False)
    age=models.PositiveIntegerField(default=18, blank=False)
    phone_number=models.CharField(max_length=50)

# Create your models here.
class FootballClub(models.Model):
    nomi=models.CharField(max_length=100,blank=False,null=False)
    sovrinlar=models.PositiveIntegerField(default=0)
    murabbiy=models.CharField(max_length=200)
    stadion=models.CharField(max_length=200)
    tashkl_topgan_yili=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_date=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomi
    