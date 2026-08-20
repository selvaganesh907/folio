from django.contrib import admin
from django.urls import path
from . import views
from .views import contact_view




urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    
    
    path('psbutton/', views.psbutton, name='psbutton'),
]