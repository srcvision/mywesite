from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('submit/', views.submit, name='submit'), 
    path('submissions/', views.submissions, name='submissions'),  
]
