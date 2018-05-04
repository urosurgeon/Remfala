from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date= models.DateField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]


    def pub_date_pretty(self):
        return self.pub_date.strftime("Published on  %A %d,  %B %Y")
