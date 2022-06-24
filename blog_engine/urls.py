from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='main'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='details'), 
]

