from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from skills.views import DashboardView

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('skills/', include('skills.urls')),
    path('goals/', include('goals.urls')),
    path('achievements/', include('achievements.urls')),
    path('api/', include('skills.api_urls')),
    path('api/', include('goals.api_urls')),
    path('api/', include('achievements.api_urls')),
    path('', DashboardView.as_view(), name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







