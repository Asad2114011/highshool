from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class NewsCard(models.Model):
    title=models.CharField(max_length=200)
    image=CloudinaryField('news_card')
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Result(models.Model):
    exam_name=models.CharField(max_length=100)
    class_name=models.CharField(max_length=100)
    year=models.IntegerField()
    file=models.FileField(upload_to='results/')
    published_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.class_name} - {self.exam_name}"
    
class class_routine(models.Model):
    class_name=models.CharField(max_length=100)
    routine=models.FileField(upload_to='class_routine/')
    published_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.class_name} Routine"
    
class class_syllabus(models.Model):
    class_name=models.CharField(max_length=100)
    syllabus=models.FileField(upload_to='class_routine/')
    published_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.class_name} Routine"


class HomepageCarousel(models.Model):
    image = CloudinaryField('carousel_homepage')

    def __str__(self):
        return f"Homepage Image {self.id}"


class PlaygroundCarousel(models.Model):
    image = CloudinaryField('carousel_playground')

    def __str__(self):
        return f"Playground Image {self.id}"


class LibraryCarousel(models.Model):
    image = CloudinaryField('carousel_library')

    def __str__(self):
        return f"Library Image {self.id}"


class ScienceLabCarousel(models.Model):
    image = CloudinaryField('carousel_science_lab')

    def __str__(self):
        return f"Science Lab Image {self.id}"


class UniformCarousel(models.Model):
    image = CloudinaryField('carousel_uniform')

    def __str__(self):
        return f"Uniform Image {self.id}"
