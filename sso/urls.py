from django.urls import path
from sso import views
from rest_framework.routers import DefaultRouter

my_router = DefaultRouter()

my_router.register(r'register', views.RegisterUserViewset, base_name='Register')

# urlpatterns = [
    
# ]