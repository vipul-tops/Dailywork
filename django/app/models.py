from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self) -> str:
        return self.name