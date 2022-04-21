from django.shortcuts import render
from .models import Cardetails
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'users/index.html')
def check(request):
    return render(request,'users/checkar.html')
def carcheck(request):
    if request.method=="POST":
        carno=request.POST['carno']
        try:
            a=Cardetails.objects.get(carno=carno)
        except:
            a=None
        if a==None:
            messages.info(request, 'car bearing this no is not present in the system',
                          extra_tags='Changes are not saved yet')
            return render(request, 'users/checkcar.html')
        else:
            if a.onrent=="No":
                messages.info(request, 'No, this car is not on rent yet.',
                              extra_tags='Changes are not saved yet')
                return render(request, 'users/checkcar.html')
            else:
                messages.info(request, 'Yes this car is on rent.',
                              extra_tags='Changes are not saved yet')
                return render(request, 'users/checkcar.html')
    else:
        return render(request,'users/checkcar.html')



def savedata(request):
    if request.method=="POST":
        carno=request.POST['carno']
        carmodel=request.POST['carmodel']
        carcolor=request.POST['carcolor']
        seatingcapacity=request.POST['seatingcapacity']
        carcompany=request.POST['carcompany']
        ownermobileno=request.POST['ownermobileno']
        cartype=request.POST['cartype']
        cargears=request.POST['cargears']
        price=request.POST['price']
        carimage=request.FILES['carimage']
        carimagefront=request.FILES['carimagefront']
        carimageback=request.FILES['carimageback']
        carimageleft=request.FILES['carimageleft']
        carimageright=request.FILES['carimageright']
        try:
            car=Cardetails.objects.get(carno=carno)
        except:
            car=None
        if car!=None:
            messages.info(request, 'This car number is Invalid or is not Unique',
                          extra_tags='Changes are not saved yet')
            return render(request,'users/index.html')
        else:
            Cardetails.objects.create(carno=carno,carmodel=carmodel,carcolor=carcolor,seatingcapacity=seatingcapacity,carcompany=carcompany,ownermobileno=ownermobileno
                                      ,cartype=cartype,cargears=cargears,price=price,carimage=carimage,carimagefront=carimagefront,carimageright=carimageright,
                                      carimageleft=carimageleft,carimageback=carimageback)



            messages.info(request, 'Your details are sucessfully saved in the database',
                          extra_tags='Changes are not saved yet')
            return render(request, 'users/index.html')





    else:
        return render(request,'users/index.html')
