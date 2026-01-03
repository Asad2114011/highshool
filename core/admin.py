from django.contrib import admin
from . models import NewsCard,Result,class_routine,class_syllabus

# Register your models here.

admin.site.register(NewsCard)
admin.site.register(Result)
admin.site.register(class_routine)
admin.site.register(class_syllabus)