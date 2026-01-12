from django.shortcuts import render,get_object_or_404
from . models import NewsCard,Result,class_routine,class_syllabus,HomepageCarousel,LibraryCarousel,ScienceLabCarousel,UniformCarousel,PlaygroundCarousel
from django.core.paginator import Paginator
from notices.models import Notice
from django.http import FileResponse
import calendar
from datetime import date



# Create your views here.
def home(request):
    newscard=NewsCard.objects.all().order_by('-date')[:4]
    notice=Notice.objects.all().order_by('-created_at')[:3]
    carousal=HomepageCarousel.objects.all()
    return render(request,'home.html',{'newscard':newscard,'notice':notice,'carsl':carousal})

def news_details(request,pk):
    card=get_object_or_404(NewsCard,pk=pk)
    return render(request,'news_detail.html',{'card':card})

def all_news(request):
    cards=NewsCard.objects.all().order_by('-date')
    paginator=Paginator(cards,8)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'all_news.html',{'page_obj':page_obj})

def library(request):
    carousal=LibraryCarousel.objects.all()
    return render(request,'library.html',{'carsl':carousal})

def playground(request):
    carousal=PlaygroundCarousel.objects.all()
    return render(request, 'playground.html',{'carsl':carousal})

def science_lab(request):
    carousal=ScienceLabCarousel.objects.all()
    return render(request,'science_lab.html',{'carsl':carousal})

def student_uniform(request):
    carousal=UniformCarousel.objects.all()
    return render(request,'student_uniform.html',{'carsl':carousal})

def result_list(request):
    result=Result.objects.all().order_by('-published_date')

    paginator=Paginator(result,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'result_list.html',{'page_obj':page_obj})

def download_result(request,pk):
    result=get_object_or_404(Result,pk=pk)
    response=FileResponse(result.file.open('rb'),as_attachment=True,filename=f"{result.class_name}_{result.exam_name}.pdf")
    return response

def routine_list(request):
    routine=class_routine.objects.all().order_by('-published_date')

    paginator=Paginator(routine,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'routine_list.html',{'page_obj':page_obj})

def routine_download(request,pk):
    routine=get_object_or_404(class_routine,pk=pk)
    return FileResponse(routine.routine.open('rb'),as_attachment=True)


def syllabus_list(request):
    syllabus=class_syllabus.objects.all().order_by('-published_date')

    paginator=Paginator(syllabus,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'syllabus_list.html',{'page_obj':page_obj})

def syllabus_download(request,pk):
    syllabus=get_object_or_404(class_syllabus,pk=pk)
    return FileResponse(syllabus.syllabus.open('rb'),as_attachment=True)

def academic_calendar(request):
    today = date.today()
    year = today.year
    month = today.month
    day = today.day

    cal = calendar.monthcalendar(year, month)

    context = {
        'calendar': cal,
        'year': year,
        'month': calendar.month_name[month],
        'today': day,
    }
    return render(request, 'academic_calendar.html', context)