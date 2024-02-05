from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email1']
        password=request.POST['pass1']
        password2=request.POST['pass2']
        if password!=password2:
            messages.error(request,"Password is not matching")
            return render(request,"authentication/signup.html")
        try:
            if User.objects.get(username=email):
                 messages.error(request,"emial.already exist")
                 return render(request,"authentication/signup.html")
            
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        
        user.save()

        

        messages.error(request,"user created")
    return render(request,"authentication/signup.html")

def handleLogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']

        
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect ('/')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/auth/login')

    return render(request,"authentication/login.html")


def handleLogout(request):
    logout(request)
    # messages.info(request,"Logout Success")
    return redirect('/auth/login')