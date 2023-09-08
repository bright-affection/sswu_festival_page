from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Info
from .forms import InfoForm
from django.contrib.auth.decorators import login_required

# 메인페이지
def mainpage(request):
    return render(request, 'mainpage.html')

# 관리자 로그인
def administrator(request):
    if request.method == 'POST':
        username = request.POST['custom_id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 로그인 성공시 메인페이지로 이동
            return redirect('mainpage:mainpage')
        else:
            return render(request, 'administrator.html', {'error': 'username or password is incorrect.'})
    return render(request, 'administrator.html')


def info_list(request):
    infos = Info.objects.all()
    return render(request, 'info.html', {'infos': infos})


# info 작성 처리
@login_required()
def info_write(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            info = Info()
            info.title = form.cleaned_data['title']
            info.content = form.cleaned_data['content']
            info.image = form.cleaned_data['image']
            info.save()
            return redirect('mainpage:info')
    else:
        form = InfoForm()
    return render(request, 'info_write.html', {'form': form})

# info 상세보기
def info_post(request, info_id):
    info = get_object_or_404(info, pk=info_id)
    return render(request, 'info_post.html', {'info': info})
