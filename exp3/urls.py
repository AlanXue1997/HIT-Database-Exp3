from django.urls import path

from . import views

app_name = 'exp3'
urlpatterns = [
    path('', views.login, name='login'),
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('<int:user_id>/changeInfo/', views.changeInfo, name='changeInfo'),
    path('<int:pk>/education', views.EducationView.as_view(), name='education'),
    path('<int:education_id>/changeEducationInfo/', views.changeEducationInfo, name='changeEducationInfo'),
    path('<int:education_id>/deleteEducationInfo/', views.deleteEducationInfo, name='deleteEducationInfo'),
    path('<int:user_id>/newEducationInfo/', views.newEducationInfo, name='newEducationInfo'),
    path('<int:pk>/work', views.WorkView.as_view(), name='work'),
    path('<int:work_id>/changeWorkInfo/', views.changeWorkInfo, name='changeWorkInfo'),
    path('<int:work_id>/deleteWorkInfo/', views.deleteWorkInfo, name='deleteWorkInfo'),
    path('<int:user_id>/newWorkInfo/', views.newWorkInfo, name='newWorkInfo'),
]
