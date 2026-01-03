from django.db import models

# Create your models here.
class NewsCard(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='news_card/')
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
