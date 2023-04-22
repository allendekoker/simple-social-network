from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
]
