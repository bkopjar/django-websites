from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date_published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    comment = models.CharField(max_length = 1000)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.name


