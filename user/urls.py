from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, RetrieveUserView, DashboardView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', RetrieveUserView.as_view(), name='me'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
 path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
