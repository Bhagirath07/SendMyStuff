from django.contrib import admin
from .models import *

admin.site.register(UserLogin)
admin.site.register(ClientReg)
admin.site.register(TransReg)
admin.site.register(OwnerReg)

# Register your models here.
