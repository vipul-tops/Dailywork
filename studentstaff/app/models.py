from django.db import models

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Staff(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.ManyToManyField(Subject, related_name='staff')

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.ManyToManyField(Subject, related_name='student')

	def __str__(self):
		return self.name