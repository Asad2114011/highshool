from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Notice(models.Model):
    title=models.CharField(max_length=200)
    image=CloudinaryField('notice_img',blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    