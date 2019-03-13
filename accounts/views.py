from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from datetime import datetime



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'نام کاربری شما قبلا ثبت شده')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'ایمیل شما قبلا ثبت شده')
                    return redirect('register')

                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                user.save()
                messages.success(request, 'ثبت نام شما با موفقیت انجام شد')
                return redirect('register')

        else:
            messages.error(request, 'رمز عبور شما مشابه هم نیستند')
            return redirect('register')

    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'به پنل کاربری خود منتقل میشوید')
            return render(request, 'account/dashboard.html')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور خود را اشتباه وارد کردید')
            return redirect('login')
    else:
        return render(request, 'account/login.html')


def dashboard(request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']
        newpassword1 = request.POST ['password1']
        newpassword2 = request.POST ['password2']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            if newpassword1 == newpassword2:
                users = User.objects.filter(username=username)
                user.set_password(newpassword1)
                user.save()
                messages.success(request,'رمز عبور شما تغییر کرد')
                auth.login(request, user)
                return redirect('dashboard')
            else :
                messages.error(request,'رمز عبور یکی نیست')
                return redirect('dashboard')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور خود را اشتباه وارد کردید')
            return redirect('login')        

    else :
        return render(request,'account/dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
