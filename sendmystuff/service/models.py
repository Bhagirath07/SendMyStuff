from django.db import models

class UserLogin(models.Model):                      # User Login
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)

class ClientReg(models.Model):                      # Client Registration
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)
    company = models.CharField(max_length=30)
    uidaino = models.IntegerField()

class TransReg(models.Model):                       # Transporter Registration
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.CharField(max_length=10)
    conpass = models.CharField(max_length=10)
    company = models.CharField(max_length=30)
    nouidai = models.IntegerField()
    nogst = models.IntegerField()
    nopan = models.IntegerField()

class OwnerReg(models.Model):                       # Fleet Owner Registration
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)
    company = models.CharField(max_length=30)
    uidaino = models.IntegerField(default='')
    gst = models.IntegerField(default='')
    truck = models.IntegerField(default='')
    driver = models.IntegerField()
    route = models.IntegerField(default='')
    address = models.CharField(max_length=200,default='')






