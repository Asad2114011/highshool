from django.db import models
from cloudinary.models import CloudinaryField


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    photo = CloudinaryField('teachers', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = CloudinaryField('staff',blank=True)
    phone = models.CharField(max_length=20, blank=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.name


class GoverningBody(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = CloudinaryField('governing_body',blank=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.name
