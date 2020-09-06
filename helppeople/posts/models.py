from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=250)
    img= models.ImageField(upload_to='pics')
    desc = models.TextField()
    people = models.IntegerField()
    conctact = models.TextField()

