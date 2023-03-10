from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='core/signin.html'), name="signin"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]