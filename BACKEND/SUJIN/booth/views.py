from django.shortcuts import render
from .models import Booth
from django.db.models import Q

def boothinfo(request):
    if request.method == 'GET':
        booth_list = Booth.objects.all().order_by('name')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'boothinfo.html', context)
    else:
        #검색어
        if 'search' in request.POST:
            searched = request.POST['search']    
            booth_list = Booth.objects.filter(name__icontains=searched).order_by('name')
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
    
