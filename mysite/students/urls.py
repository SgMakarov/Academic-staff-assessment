from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('register/', views.signup, name='student_registration'),
]
