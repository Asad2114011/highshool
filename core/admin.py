from django.contrib import admin
from . models import NewsCard,Result,class_routine,class_syllabus,HomepageCarousel,PlaygroundCarousel,UniformCarousel,LibraryCarousel,ScienceLabCarousel

# Register your models here.

admin.site.register(NewsCard)
admin.site.register(Result)
admin.site.register(class_routine)
admin.site.register(class_syllabus)
admin.site.register(HomepageCarousel)
admin.site.register(ScienceLabCarousel)
admin.site.register(PlaygroundCarousel)
admin.site.register(UniformCarousel)
admin.site.register(LibraryCarousel)