from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list.as_view(), name='blog'),
    path('<slug>/', views.post_detail.as_view(), name='post_detail'),
]