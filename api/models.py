from django.db import models

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
    