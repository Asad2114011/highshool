from django.shortcuts import render,get_object_or_404
from . models import Notice
from django.core.paginator import Paginator
# Create your views here.

def notice_list(request):
    notices=Notice.objects.all().order_by('-created_at')
    paginator=Paginator(notices, 5)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'notice_list.html',{'page_obj':page_obj})

def notice_detail(request,pk):
    notice=get_object_or_404(Notice,pk=pk)
    return render(request,'notice_detail.html',{'notice':notice})