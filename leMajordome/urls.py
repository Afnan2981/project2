from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static
from user.views import RegisterView  # Adjust the import path based on your actual project structure

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('auth/user/', include('user.urls')),
    path('api/listing/', include('listing.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('user/', include('user.urls', namespace='user')),  # Assuming 'user' is your app name

    # Add the following lines for login and register
    path('auth/user/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/user/register/', RegisterView.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
