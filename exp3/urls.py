from django.urls import path

from . import views

app_name = 'exp3'
urlpatterns = [
    path('', views.login, name='login'),
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/education', views.EducationView.as_view(), name='education'),
    path('<int:user_id>/changeInfo/', views.changeInfo, name='changeInfo'),
    path('<int:education_id>/changeEducationInfo/', views.changeEducationInfo, name='changeEducationInfo'),
    path('<int:education_id>/deleteEducationInfo/', views.deleteEducationInfo, name='deleteEducationInfo'),
    path('<int:user_id>/newEducationInfo/', views.newEducationInfo, name='newEducationInfo'),
]
