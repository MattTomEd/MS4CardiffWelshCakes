from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list.as_view(), name='blog'),
    # path('<slug>/', views.post_content.as_view(), name='post_content'),
    path('<slug:slug>/', views.post_detail, name='post_content'),
]