from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date= models.DateField()
    image = models.ImageField(upload_to='images/')

