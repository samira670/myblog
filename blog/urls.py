from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Example URL for the homepage
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Example for post details
]