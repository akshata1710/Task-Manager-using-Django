from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("user_signup",views.user_signup,name="user_signup"),
    path("user_login", views.user_login, name="user_login"),
    path("create",views.create,name="create"),
    path("user_logout",views.user_logout,name="user_logout"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("user_np/",views.user_np,name="user_np"),

]
