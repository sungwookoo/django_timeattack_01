from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.sign_up_view),
    path('user/register', views.sign_up_view),
]