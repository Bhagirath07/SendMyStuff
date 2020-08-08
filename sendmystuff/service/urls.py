from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('cRegistration/',views.clientReg, name='client_reg'),
    path('tRegistration/',views.transReg, name='trans_reg'),
    path('oRegistration/',views.ownerReg, name='owner_reg'),
]