from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Item
# Create your views here.

def allprod(request):
    obj = Item.objects.all()
    return render(request,'home.html',{'prod':obj})

def register_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['password1']
        try:
            if password == c_password:
                # if User.objects.filter(username=username).exists():
                #     messages.info(request, "Username Taken")
                #     return redirect('register_user')
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('store:login_user')

            # else:
            #     messages.info(request, "Password Not Matching")
            #     return redirect('register_user')
        except Exception as e:
            return redirect('store:register_user')

    return render(request, 'register.html')

def login_user(request):

        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # username=request.POST['username']
            # password = request.POST['password']
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return render(request,'button.html')

            else:
                messages.info(request,"invalid credentials")
                return redirect('store:login_user')

        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

# def newform(request):
#     return render(request,'newform.html')


def submit_form(request):
    return render(request,'submit.html')



