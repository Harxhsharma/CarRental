from django.urls import path, include
from . import views
urlpatterns = [
path("",views.index,name="index"),
path("login",views.login,name="login"),
path("signup",views.signup,name="signup"),
path("register",views.register,name="register"),
    path("home",views.home,name="home"),
path("loginn",views.loginn,name="loginn"),
]