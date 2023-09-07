from django.shortcuts import render
from .models import Booth
from django.db.models import Q

# Create your views here.
# def boothinfo(request):
#     booth_list = Booth.objects.all().order_by('name')
#     context = {
#         'booth_list' : booth_list
#     }
#     return render(request, 'visitor.html', context)

# def goods_filter(request):
#     date = request.GET.getlist('size', None)
#     time = request.GET.getlist('color', None)
#     kind = request.GET.getlist('kind', None)

#     q=Q()
#     if date:
#         q &= Q(date__in = time)
#     if time:
#         q &= Q(time__in = time)
#     if kind:
#         q &= Q(kind__in = kind)
                
#     booth_list = Booth.objects.filter(q).order_by('name')
#     context = {
#         'booth_list' : booth_list
#     }
#     return render(request, 'visitor.html', context)

#합친거
def boothinfo(request):
    if request.method == 'GET':
        booth_list = Booth.objects.all().order_by('name')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'visitor.html', context)
    else:
        #필터가 적용돼서 post요청이 온다면
        date = request.GET.getlist('size', None)
        time = request.GET.getlist('color', None)
        kind = request.GET.getlist('kind', None)

        q=Q()
        if date:
            q &= Q(date__in = time)
        if time:
            q &= Q(time__in = time)
        if kind:
            q &= Q(kind__in = kind)
                    
        booth_list = Booth.objects.filter(q).order_by('name')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'visitor.html', context)
    
#검색어 입력
def boothsearch(request):
    if request.method == 'GET':
        booth_list = Booth.objects.all().order_by('name')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'visitor.html', context)
    else:
        #검색어가 입력돼서 post요청이 온다면
        searched = request.POST['searched']        
        booth_list = Booth.objects.filter(name__contains=searched).order_by('name')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'visitor.html', {'searched': searched, 'context': context})
