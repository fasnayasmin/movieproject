from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)
    years=models.IntegerField()
    img=models.ImageField(upload_to='img',null=True,blank=True)

    def __str__(self):
        return self.name
