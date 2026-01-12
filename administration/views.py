from django.shortcuts import render
from .models import Teacher,Staff,GoverningBody


# Create your views here.

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def staff(request):
    staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': staff})

def governing_body(request):
    governing_body = GoverningBody.objects.all()
    return render(request, 'governing_body.html', {'governing_body': governing_body})
