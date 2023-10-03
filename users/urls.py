from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit-profile"),
    path('register/', views.registration_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),

]