from django.shortcuts import render,redirect
from users.models import Cardetails
from django.contrib import messages
from .models import Rent
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    company = Cardetails.objects.filter(onrent="No")
    print(company)
    return render(request, 'clients/index.html',{'companies':company})

def pickcar(request):
    if request.method=="POST":
        username=request.POST['username']
        carno=request.POST['company_name']
        print(carno,"Car No")
        try:
            a=User.objects.get(username=username)
        except:
            a=None


        if a!=None:
            if a.rent.bookedcar!="No":
                messages.info(request, 'You have already rented a car',
                              extra_tags='Changes are not saved yet')
                company = Cardetails.objects.filter(onrent="No")

                return render(request, 'clients/index.html', {'companies': company})
            else:
                try:
                    car=Cardetails.objects.get(carno=carno)
                except:
                    car=None

                if car==None:
                    messages.info(request, 'You have entered wrong number.',
                                  extra_tags='Changes are not saved yet')
                    company = Cardetails.objects.filter(onrent="No")

                    return render(request, 'clients/index.html', {'companies': company})


                return render(request, 'clients/details.html',{'car':car})




        else:
            messages.info(request, 'Invalid username',
                          extra_tags='Changes are not saved yet')
            return render(request,'clients/index.html')


    else:
        return render(request,'clients/index.html')
def dealdone(request):
    if request.method=="POST":
        username = request.POST['username']
        carno = request.POST['company_name']

        till=request.POST['till']
        fromm=request.POST['from']
        a = User.objects.get(username=username)
        a.rent.bookedcar="Yes"
        a.rent.fromm=fromm
        a.rent.to=till
        a.rent.carnumber=carno
        a.rent.save()
        #print(carno,"Hellow world")
        b=Cardetails.objects.get(carno=carno)
        b.onrent="Yes"
        b.rentedto=username
        b.fromm=fromm
        b.to=till
        b.save()
        a = User.objects.get(username=username)

        messages.info(request, 'You have sucessfully booked the car',
                      extra_tags='Changes are not saved yet')
        return render(request, 'clients/final.html')
def home(request):
    return redirect('/')

