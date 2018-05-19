from django.urls import path

from . import views

app_name = 'exp3'
urlpatterns = [
    path('', views.login, name='login'),
    path('<int:pk>/', views.IndexView.as_view(), name='index'),

    # Info
    path('<int:user_id>/changeInfo/', views.changeInfo, name='changeInfo'),

    # Education
    path('<int:pk>/education', views.EducationView.as_view(), name='education'),
    path('<int:education_id>/changeEducationInfo/', views.changeEducationInfo, name='changeEducationInfo'),
    path('<int:education_id>/deleteEducationInfo/', views.deleteEducationInfo, name='deleteEducationInfo'),
    path('<int:user_id>/newEducationInfo/', views.newEducationInfo, name='newEducationInfo'),

    # Work
    path('<int:pk>/work', views.WorkView.as_view(), name='work'),
    path('<int:work_id>/changeWorkInfo/', views.changeWorkInfo, name='changeWorkInfo'),
    path('<int:work_id>/deleteWorkInfo/', views.deleteWorkInfo, name='deleteWorkInfo'),
    path('<int:user_id>/newWorkInfo/', views.newWorkInfo, name='newWorkInfo'),

    # Diary
    path('<int:user_id>/diaryList', views.diaryList, name='diaryList'),
    path('<int:pk>/newDiary', views.NewDiaryView.as_view(), name='newDiary'),
    path('<int:user_id>/newDiary/push', views.pushNewDiary, name='pushNewDiary'),
    path('<int:user_id>/diary/<int:diary_id>/', views.diarypage, name='diary'),
    path('<int:user_id>/editDiary/<int:diary_id>/', views.editDiary, name='editDiary'),
    path('<int:user_id>/editDiary/<int:diary_id>/push', views.pushEditDiary, name='pushEditDiary'),
    path('<int:user_id>/editDiary/<int:diary_id>/delete', views.deleteEditDiary, name='deleteEditDiary'),

    # Follow
    path('<int:user_id>/follow', views.follow, name='follow'),
    path('<int:user_id>/follow/add', views.addFollow, name='addFollow'),
    path('<int:user_id>/follow/unfollow/<int:u_id>', views.unfollow, name='unfollow'),
    path('<int:user_id>/follow/add/<int:u_id>', views.doAddFollow, name='doAddFollow'),
]
