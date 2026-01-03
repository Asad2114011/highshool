from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('news/<int:pk>/',views.news_details,name='news_detail'),
    path('all_news/',views.all_news,name='all_news'),
    path('library/',views.library,name='library'),
    path('playground/',views.playground,name='playground'),
    path('science_lab/',views.science_lab,name='science_lab'),
    path('student_uniform/',views.student_uniform,name='student_uniform'),
    path('results/',views.result_list,name='results'),
    path('result/download/<int:pk>/',views.download_result,name='download_result'),
    path('routine/',views.routine_list,name='routine_list'),
    path('routine/download/<int:pk>/',views.routine_download,name='routine_download'),
    path('syllabus/',views.syllabus_list,name='syllabus_list'),
    path('syllabus/download/<int:pk>/',views.syllabus_download,name='syllabus_download'),
    path('academic-calendar/',views.academic_calendar,name='academic_calendar'),
]
