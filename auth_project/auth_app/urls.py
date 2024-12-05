from django.urls import path
# 1 - lo vamos a llamar para llamar a las vista de usuario y la tabla es user
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #1 LoginView viene de django
    path('login/', auth_views.LoginView.as_view(template_name='auth_app/login.html'), name='login'),
    #2 LogoutView viene de django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
]