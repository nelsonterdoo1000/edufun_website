from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
# Create your views here.
def home(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        sex = request.POST['sex']
        phone = request.POST['phone']
        message =  request.POST['message']
        try:
            Trainee.objects.create(fname=fname,lname=lname,sex=sex,phone=phone,message=message)        
        except:
            return HttpResponse("<h1>You did not enter the required details</h1>")
    return render(request,'register.html')