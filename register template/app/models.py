from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.PositiveIntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    imgname = models.CharField(max_length=50)
    addimg = models.ImageField(upload_to="img/")

    def __str__(self):
        return self.imgname