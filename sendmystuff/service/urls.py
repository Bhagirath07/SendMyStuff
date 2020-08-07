from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('cRegistration/',views.clientReg, name='signup'),
    path('tRegistration/',views.transReg, name='signup'),
    path('oRegistration/',views.ownerReg, name='signup'),
]