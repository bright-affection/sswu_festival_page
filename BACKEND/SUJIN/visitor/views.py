from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Visitor

# Create your views here.
def visitor_write(request):
    if request.method == 'GET':
        return render(request, 'visitor-write.html')
    else:
        content = request.POST.get('content')
        nickname = request.POST.get('nickname')
        code = request.POST.get('code')
        Visitor.objects.create(
            nickname=nickname,
            content = content,
            code = code,
        )
        return redirect('/visitor')
    
def visitor(request):
    visitor_list = Visitor.objects.all().order_by('-date')[:3]
    # [8:10] 9, 10번째 글
    context = {
        'visitor_list' : visitor_list
    }
    return render(request, 'visitor.html', context)

def visitor_more(request, page):
    visitor_list = Visitor.objects.all().order_by('-date')[3 * page : 3 * (page+1)]
    context = {
        'visitor_list' : visitor_list
    }
    return render(request, 'visitor.html', context)

# ---------ajax 테스트 -----------