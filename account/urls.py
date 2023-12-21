from django.urls import path
from .views import Signup,Login,Logout

urlpatterns = [
    path('',Signup,name='signup'),
    path('Login/',Login,name='Login'),
    path('Logout',Logout,name='Logout')
]
