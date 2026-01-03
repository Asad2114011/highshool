from django.shortcuts import render

# Create your views here.
def governing_body(request):
    return render(request,'governing_body.html')

def teachers(request):
    return render(request,'teachers.html')

def staff(request):
    return render(request,'staff.html')