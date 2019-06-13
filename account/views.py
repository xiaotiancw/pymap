from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def account_login(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')

    if request.method == 'POST':
        '''登录'''
        '''用户验证'''
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username)
        print(password)
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('account:account_index')
                else:
                    return render(request, 'account/login.html', {'error_msg': '用户失效！'})
            else:
                return render(request, 'account/login.html', {'error_msg': '用户名或密码错误'})
        else:
            return render(request, 'account/login.html', {'error_msg': '用户不存在'})





@login_required()
def account_index(request):
    '''首页'''
    return render(request, 'account/index.html')




@login_required()
def account_welcome(request):
    '''欢迎页'''
    return render(request, 'account/welcome.html')





def account_logout(request):
    '''退出登陆'''
    logout(request)
    return redirect('account:account_login')
