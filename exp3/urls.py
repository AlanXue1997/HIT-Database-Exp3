from django.urls import path

from . import views

app_name = 'exp3'
urlpatterns = [
    path('', views.login, name='login'),
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
]
