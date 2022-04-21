from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from clients.models import Rent
# Create your views here.
def index(request):
    return render(request,'company/index.html')
def login(request):
    return render(request,'company/login.html')
def signup(request):
    return render(request,'company/signup.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        lastname = request.POST['lastname']
        password1 = request.POST['psw']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:

                user = User.objects.create_user(username=username, last_name=lastname, first_name=first_name,
                                                password=password1, email=email)
                user.save()

                Rent.objects.create(user=user)
                messages.info(request, "You have sucessfully registered yourself! Please login here.")
                return render(request,'company/login.html')

        else:
            messages.info(request, 'Password not Matching')
            return redirect('signup')
    else:
        return render(request, 'company/signup.html')
def home(request):
    return redirect('/')
def loginn(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user==None:
            messages.info(request, 'Invalid credentials! Please try again', extra_tags='login_error')

            return render(request, 'company/login.html')
        else:
            messages.info(request, 'Hi Mr. ' + user.first_name + ' we welcomes you in carrentals.co ',
                          extra_tags='login_error')
            return render(request, 'company/portal.html')
        #style="background-color:#8BC6EC;background-image:linear-gradient(135deg, #8BC6EC 0%, #9599E2 100%);width:100%;height:100%"
    else:
        return render(request, 'company/login.html')
from django.shortcuts import render

# Create your views here.
