# from django.urls import path
from sso import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

my_router = DefaultRouter()

my_router.register(r'register', views.RegisterUserViewset, base_name='Register')
my_router.register(r'login', views.LoginViewset, base_name='Login')

urlpatterns = my_router.urls