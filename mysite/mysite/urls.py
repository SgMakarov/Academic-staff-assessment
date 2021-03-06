"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from .views import AuthView
from django.contrib.auth import views as auth_views
from survey.views import IndexView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('survey/', include('survey.urls')),
    path('students/', include('students.urls')),
    path('login/oauth/', AuthView.as_view(), name="oauth"),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name='index.html'), name='home'),
]
