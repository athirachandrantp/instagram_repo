from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
    path('create_post/', views.create_post, name="create_post"),
    path('update_post/<str:pk>/', views.update_post, name="update_post"),
    path('delete_post/<str:pk>/', views.delete_post, name="delete_post"),
    path('likes/<str:pk>/', views.post_likes, name="post_like"),
    path('user-post/<str:pk>/', views.user_post, name="user_post"),
    path('delete_comment/<str:pk>/', views.delete_comment,
         name="delete_comment"),

]