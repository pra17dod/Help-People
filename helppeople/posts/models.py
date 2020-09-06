from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')
    target_people = models.IntegerField()
    isDonar = models.BooleanField(default=False)
    desc = models.TextField()
    contact = models.IntegerField()
 