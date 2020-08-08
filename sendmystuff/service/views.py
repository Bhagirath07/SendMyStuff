from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *                   # import All Classes
from django.contrib import messages

def login(request):                         # User Login
    if request.POST :
        email = request.POST['email']
        password = request.POST['password']
        count = UserLogin.objects.filter(email=email,password=password).count()

        if count > 0:
            return HttpResponse("Login Successfully......")
        else:
            messages.error(request,'Invalid Email and Passowrd')
            return redirect('login')
    return render(request,'registration/login.html')

def clientReg(request):                     # Client Registration
    if request.POST :
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        dob = request.POST['dob']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        company = request.POST['company']
        uidaino = request.POST['uidaino']

        obj = ClientReg(name=name,email=email,contact=contact,dob=dob,password=password,cpassword=cpassword,company=company,uidaino=uidaino)
        obj.save()
        messages.success(request, 'You Are Registration Successfully !')
        return redirect("login")
    return render(request,'registration/client.html')

def transReg(request):                      # Transporter Registration
    if request.POST :
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        dob = request.POST['dob']
        password = request.POST['password']
        conpass = request.POST['conpass']
        company = request.POST['company']
        nouidai = request.POST['nouidai']
        nogst = request.POST['nogst']
        nopan = request.POST['nopan']

        trans = TransReg(name=name,email=email,contact=contact,dob=dob,password=password,
                        conpass=conpass,company=company,nouidai=nouidai,nogst=nogst,nopan=nopan)
        trans.save()
        messages.success(request, 'You Are Registration Successfully !')
        return redirect("login")
    return render(request,'registration/transporter.html')

def ownerReg(request):                  # Fleet Owner Registration
    if request.POST :
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        dob = request.POST['dob']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        company = request.POST['company']
        uidaino = request.POST['uidaino']
        gst = request.POST['gst']
        truck = request.POST['truck']
        driver = request.POST['driver']
        route = request.POST['route']
        address = request.POST['address']

        fleetown = OwnerReg(name=name,email=email,contact=contact,dob=dob,password=password,
                            cpassword=cpassword,company=company,uidaino=uidaino,gst=gst,
                            truck=truck,driver=driver,route=route,address=address)
        fleetown.save()
        messages.success(request, 'You Are Registration Successfully !')
        return redirect("login")
    return render(request,'registration/owner.html')



