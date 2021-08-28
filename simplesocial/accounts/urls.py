from django.urls import path

# For Login/Logout inbuilt views provided
from django.contrib.auth import views as auth_views
from . import views

# TEMPLATE TAGGING
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]