"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from escola.urls import aluno_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('escola/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('escola/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('escola/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('escola/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('escola/token/refresh', TokenRefreshView.as_view(),  name='token_refresh'),
    path('escola/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('escola/', include(aluno_urls))
]
