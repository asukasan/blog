from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('reveal/', views.reveal, name='reveal'),
]
