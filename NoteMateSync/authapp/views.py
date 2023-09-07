from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method =="POST":
        get_username=request.POST.get('username')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password!=get_confirm_password:
            messages.info(request,'psssword is not matching')
            return redirect('/auth/signup/')


        try:
            if User.objects.get(username=get_username):
                messages.warning(request,'email is already taken')
                return redirect('/auth/signup/')
        except Exception as identifer:
            pass
        myuser = User.objects.create_user(get_username,get_username,get_password)
        myuser.save()
        messages.success(request,'useer has been created please login')
        return redirect('/auth/login/')
    return render(request,'signup.html')


def login(request):
    return render(request,'login.html')

def logout(request):
    return redirect('/authapp/login')