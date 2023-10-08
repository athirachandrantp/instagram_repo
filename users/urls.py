from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_profile, name="profile"),
    path('user/<str:pk>/', views.single_user_profile, name="single-profile"),
    path('edit_profile/', views.edit_profile, name="edit-profile"),
    path('register/', views.registration_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('follow/<str:pk>/', views.follow_profile, name="follow_user"),
    path('unfollow/<str:pk>/', views.unfollow_profile, name="unfollow_user"),
    path('followers/<str:pk>/', views.follow_users, name="followers"),
    path('following/<str:pk>/', views.following_user, name='following')

]