from django.shortcuts import render
from .models import Booth
from django.db.models import Q

def boothinfo(request):
    if request.method == 'GET':
        print("ㅎㅇㅎㅇㅎㅇ")
        booth_list = Booth.objects.all().order_by('name')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'boothinfo.html', context)
    else:
        #검색어
        if request.POST['search']:
            searched = request.POST['search']    
            print(searched)    
            booth_list = Booth.objects.filter(name__icontains=searched).order_by('name')
            print(Booth.objects.filter(name__icontains=searched).order_by('name').query)
            context = {
                'booth_list' : booth_list
            }
            return render(request, 'boothinfo.html', context)
        else:
            #필터
            date = request.POST.getlist('date', None)
            time = request.POST.getlist('time', None)
            kind = request.POST.getlist('kind', None)

            q=Q()
            if date:
                q &= Q(date__in = date)
            if time:
                q &= Q(time__in = time)
            if kind:
                q &= Q(kind__in = kind)
                        
            booth_list = Booth.objects.filter(q).order_by('name')
            context = {
                'booth_list' : booth_list
            }
            return render(request, 'boothinfo.html', context)
    
