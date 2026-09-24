from django.urls import path
from robotapp import views



urlpatterns = [
    path("", views.home, name="home"),
    # path("", views.home, name="home"),
    path('create_user/', views.register, name = "user_creation"),
    path("login/",views.login, name = "login"),
    path("dashboard/",views.dashboard, name = "dashboard"),
    path("users_list/", views.users, name="users_list"),
    path("edit_user_details/<str:pk>/", views.edit_user, name="edit_user"),
    path("delete_user/<str:pk>/", views.delete_user, name="delete_user"),
    path("logout/", views.logout, name="logout"),
    path("contact", views.contact, name= "contact")
    
    
   
 
]