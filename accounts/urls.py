from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]