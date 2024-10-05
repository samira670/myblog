from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # List all posts (homepage)
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # View individual posts
]
